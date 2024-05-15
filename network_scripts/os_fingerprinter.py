import nmap
import subprocess

def identify_os(target_ip):
    # Create a new instance of the nmap PortScanner class
    nm = nmap.PortScanner()

    # Construct the nmap command with the appropriate arguments for OS detection
    nmap_command = f"sudo nmap -O {target_ip}"

    # Execute the nmap command and capture the output
    try:
        output = subprocess.check_output(nmap_command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error executing nmap command:", e)

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    identify_os(target_ip)