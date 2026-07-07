import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
response = requests.get(URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
full_price = (float) (price_whole + price_fraction)
print(full_price)