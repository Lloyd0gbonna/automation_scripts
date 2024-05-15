import requests
from bs4 import BeautifulSoup

def count_a_tags(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags on the webpage and count them
        a_tags = soup.find_all('a')
        num_a_tags = len(a_tags)
        
        return num_a_tags
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return -1

# Prompt the user to enter the URL
url = input("Enter the URL of the website: ")

# Call the function to count the number of <a> tags
num_a_tags = count_a_tags(url)

# Check if the URL is valid and print the result
if num_a_tags != -1:
    print("Number of <a> tags on the webpage:", num_a_tags)
else:
    print("Invalid URL entered.")