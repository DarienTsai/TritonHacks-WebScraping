# Entrypoint to your webscraping starter kit
import requests
from bs4 import BeautifulSoup

# HTTP header we'll use for getting the page
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    # 'Access-Control-Max-Age': '3600',
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

"""
Get a copy of the page
"""
url = "https://www.yelp.com/search?find_desc=burger&find_loc=La+Jolla%2C+San+Diego%2C+CA&ns=1"
page = requests.get(url, headers)
scraper = BeautifulSoup(page.content, 'html.parser')

"""
Scrape the page
"""

# Get all search results
results = scraper.find_all("div", class_="container__09f24__21w3G")

# Get all star ratings
# TODO replace ' star rating' with '' in aria-label
stars = scraper.find_all("div", class_="i-stars__09f24__1T6rz")

# Get all prices
prices = scraper.find_all("span", class_="priceRange__09f24__2O6le")


# Get store names
titleContainers = scraper.find_all("div", class_="businessName__09f24__3Wql2 display--inline-block__09f24__FsgS4 border-color--default__09f24__R1nRO")

storeNames = []
for i in range(len(storeNames)):
    storeNames += titleContainers[i].find_all("a", class_="link-size--inherit__09f24__2Uj95")


# Print tests
for i in range(len(storeNames)):
    print(storeNames[i].string)

for i in range(len(stars)):
    print(stars[i]["aria-label"])

for i in range(len(prices)):
    print(prices[i].string)