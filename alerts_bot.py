import requests
from bs4 import BeautifulSoup
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def scrape_binance():
    url = "https://www.binance.com/en/support/announcement/c-48"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all('a', class_='css-6f91y1')
    alerts = []
    for title in titles[:3]:
        title_text = title.text.strip()
        if "Will List" in title_text or "lists" in title_text:
            alerts.append("[Binance] " + title_text)
    return alerts

def main():
    alerts = scrape_binance()
    for alert in alerts:
        send_telegram_message(alert)

if __name__ == "__main__":
    main()
