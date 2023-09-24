import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# Function to save content to a file
def save_content_to_file(content, file_path):
    with open(file_path, 'wb') as file:
        file.write(content)

# Function to scrape a webpage and its linked pages recursively
def scrape_webpage(url):
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Save the page content to a file in the current directory
        file_name = urlparse(url).path.strip('/').replace('/', '_') + ".html"
        file_path = os.path.join(os.getcwd(), file_name)
        save_content_to_file(response.content, file_path)

        # Find and follow links on the page (you may need to customize this)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('#'):
                absolute_url = urljoin(url, href)
                scrape_webpage(absolute_url)

# User input: URL to scrape
url_to_scrape = input("Enter the URL to scrape: ")

# Start scraping
scrape_webpage(url_to_scrape)

print("Scraping completed. Data saved in the current directory.")
