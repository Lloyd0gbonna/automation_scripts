import nmap

def scan_ports(target):
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=target, arguments='-p 1-65535 -T4 -v')  # Scan all ports with aggressive timing
        for host in nm.all_hosts():
            print(f"Host: {host}")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}")
    except nmap.PortScannerError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ")
    scan_ports(target)