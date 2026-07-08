from scrape_price import ScrapePrice
from notification_manager import NotificationManager

TARGET_URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100

scraper = ScrapePrice(TARGET_URL)
price = scraper.scrape_price()
product_full_name = scraper.scrape_product_full_name()

if price < TARGET_PRICE:
    notification_manager = NotificationManager()
    message = f"Subject:AMAZON PRICE ALERT!\n\n{product_full_name} is now ${price}\n{TARGET_URL}"
    notification_manager.send_emails(message=message)
print(price)