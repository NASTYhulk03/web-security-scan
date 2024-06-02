# crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Successfully fetched {url}")
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
    print(f"Found links: {links}")
    return links
