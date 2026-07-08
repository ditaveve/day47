# Amazon Price Tracker

Scrapes a product page for its current price and, if it drops below a target price, emails an alert with the product name, price, and link.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in this folder with:
   ```
   MY_EMAIL=your_gmail_address@gmail.com
   MY_EMAIL_PASSWORD=your_gmail_app_password
   RECEIVER_EMAIL=where_you_want_alerts_sent@example.com
   ```
   - `MY_EMAIL_PASSWORD` must be a [Gmail App Password](https://myaccount.google.com/apppasswords), not your regular account password (requires 2-Step Verification enabled on the account).
   - `RECEIVER_EMAIL` is optional — if omitted, alerts are sent to `MY_EMAIL` itself.
   - `.env` is git-ignored; never commit it.

## Tracking a different product

Edit these values at the top of [main.py](main.py):

```python
TARGET_URL = "https://www.amazon.com/..."   # the product page to watch
TARGET_PRICE = 1000                          # alert if price drops below this
TARGET_PRICE_CURRENCY = "RON"                # currency label shown in the email
```

Replace `TARGET_URL` with the Amazon product page you want to track, and set `TARGET_PRICE` to your desired threshold.

## Sending alerts to a different account

Set `RECEIVER_EMAIL` in `.env` to the address you want alerts delivered to. It can be different from `MY_EMAIL` (the sending account).

## Running

```bash
python3 main.py
```

The script checks the price once per run. To monitor continuously, schedule it (e.g. cron, a scheduled task, or a loop with a delay).
