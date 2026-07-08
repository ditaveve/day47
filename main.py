from scrape_price import ScrapePrice

scraper = ScrapePrice()
price = scraper.scrape_price()

print(price)