import subprocess

def ping_website(website):
    """
    Ping a website to check if it is reachable.
    
    Args:
        website (str): The URL of the website to ping.
        
    Returns:
        bool: True if the website is reachable, False otherwise.
    """
    try:
        # Use subprocess to run the ping command
        output = subprocess.check_output(["ping", "-c", "1", website])
        # If the ping is successful, return True
        return True
    except subprocess.CalledProcessError:
        # If there's an error (website is unreachable), return False
        return False

if __name__ == "__main__":
    # Prompt the user to enter the website URL
    website = input("Enter website URL: ")
    # Call the ping_website function and print the result
    if ping_website(website):
        print(f"{website} is reachable.")
    else:
        print(f"{website} is not reachable.")