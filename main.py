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
url = "https://www.yelp.com/search?find_desc=hot+dog&find_loc=La+Puente%2C+CA+91744&ns=1"
page = requests.get(url, headers)
scraps = BeautifulSoup(page.content, 'html.parser')


"""
Scrape the page
"""
# Get the html elements that are related to the search results
containers = scraps.find_all("div", class_="businessName__09f24__3Wql2 display--inline-block__09f24__FsgS4 border-color--default__09f24__R1nRO")

# Get the store names
stores = []
for i in range(len(containers)):
    stores += containers[i].find_all("a", class_="link-size--inherit__09f24__2Uj95")

# Print test
for i in range(len(stores)):
    print(stores[i].string)
