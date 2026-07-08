import requests
from bs4 import BeautifulSoup

class ScrapePrice:

    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

    def __init__(self, URL):
        response = requests.get(URL, headers=self.HEADERS)
        web_page = response.text
        self.soup = BeautifulSoup(web_page, "html.parser")

    def scrape_price(self):
        price_whole = self.soup.find(name="span", class_="a-price-whole").getText()
        price_fraction = self.soup.find(name="span", class_="a-price-fraction").getText()
        full_price = float(price_whole + price_fraction)
        return full_price
    
    def scrape_product_full_name(self):
        raw_title = self.soup.find(name="span", id="productTitle").getText()
        return " ".join(raw_title.split())