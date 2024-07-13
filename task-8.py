"""8.	Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions."""
import requests
from time import sleep

def fetch_url_content(url):
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            return response.content
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - URL: {url}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err} - URL: {url}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err} - URL: {url}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err} - URL: {url}")
        
        # Wait before retrying
        sleep(2)
    return None

def download_contents(urls):
    contents = {}
    for url in urls:
        print(f"Fetching URL: {url}")
        content = fetch_url_content(url)
        if content is not None:
            contents[url] = content
        else:
            print(f"Failed to fetch content from URL: {url} after 3 attempts")
    return contents

# Example usage
urls = [
    "https://www.example.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]

contents = download_contents(urls)
for url, content in contents.items():
    print(f"Content from {url}: {content[:100]}...")  # Print the first 100 characters of the content
