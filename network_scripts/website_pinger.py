import subprocess

def ping_website(website):
    try:
        output = subprocess.check_output(["ping", "-c", "1", website])
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    website = input("Enter website URL: ")
    if ping_website(website):
        print(f"{website} is reachable.")
    else:
        print(f"{website} is not reachable.")