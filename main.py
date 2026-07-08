from scrape_price import ScrapePrice
from notification_manager import NotificationManager

TARGET_URL = "https://www.amazon.com/dp/B0DNF49K1D/ref=sspa_dk_detail_2?pd_rd_i=B0DNF49K1D&pd_rd_w=orORV&content-id=amzn1.sym.3bc66c0a-cc61-4816-aa2d-e53327eaddb6&pf_rd_p=3bc66c0a-cc61-4816-aa2d-e53327eaddb6&pf_rd_r=FJHYQSRACMHXYCS90Y9R&pd_rd_wg=yKNSS&pd_rd_r=4a259fbb-a72d-497c-a133-864aac82d0c3&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1"
TARGET_PRICE = 1000
TARGET_PRICE_CURRENCY = "RON"

scraper = ScrapePrice(TARGET_URL)
price = scraper.scrape_price()
product_full_name = scraper.scrape_product_full_name()

if price < TARGET_PRICE:
    notification_manager = NotificationManager()
    message = f"Subject:AMAZON PRICE ALERT!\n\n{product_full_name} is now {price}{TARGET_PRICE_CURRENCY}\n{TARGET_URL}"
    notification_manager.send_emails(message=message)
print(price)