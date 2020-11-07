# Entrypoint to your webscraping starter kit
import requests
from bs4 import BeautifulSoup

# Web Scraping code


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    # 'Access-Control-Max-Age': '3600',
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "https://weather.com/weather/today/l/33.9955,-117.9764"
page = requests.get(url, headers)
soup = BeautifulSoup(page.content, 'html.parser')

weather_tables = soup.find_all(attrs={'title': 'Daily Forecast'})[0]
weather = weather_tables.find_all("li", class_="Column--column--2bRa6")

print(weather)
print(len(weather))
# print(len(weather))
# prints the whole page
# print(soup.prettify())