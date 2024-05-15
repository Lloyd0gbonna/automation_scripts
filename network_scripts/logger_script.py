import nmap
import logging
import ping3

# Configure logging
logging.basicConfig(filename='network_scan.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to perform port scanning
def port_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 1-65535 -sS')
    logging.info("Port scanning results for {}: {}".format(target, nm.csv()))

# Function to perform OS fingerprinting
def os_fingerprint(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    logging.info("OS fingerprinting results for {}: {}".format(target, nm.csv()))

# Function to ping a website
def ping_website(website):
    response = ping3.ping(website)
    if response is not None:
        logging.info("Ping result for {}: {} ms".format(website, response))
    else:
        logging.error("Failed to ping {}".format(website))

if __name__ == "__main__":
    targets = ['192.168.1.1', 'example.com']  # Add your target IP addresses or domain names here

    for target in targets:
        port_scan(target)
        os_fingerprint(target)
        ping_website(target)