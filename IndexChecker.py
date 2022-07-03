import time

import requests
from bs4 import BeautifulSoup
import re

from env import API_KEY

pages = [
    'https://www.youtube.com/',
    'https://vk.com/',
    'http://artprezent.com/login'
]

# https://www.scraperapi.com/quick-start-guides/python-requests-beautifulsoup-scraper/
proxies = {
  'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
}
not_indexed = re.compile("did not match any documents")

for page in pages:
    url = "https://www.google.com/search?q=site:" + page + "&hl=en"
    data = requests.get(url, proxies=proxies, verify=False)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")

    if soup(text=not_indexed):
        print("This page is NOT indexed by Google.")
    else:
        print("This page is indexed by Google.")

    time.sleep(2)
