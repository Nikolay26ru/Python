import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

URL = "https://ria.ru/world/"
DB_PATH = "news.db"
CSV_PATH = "news.csv"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
news_items = []
for item in soup.select(".list-item__content"):
    title = item.select_one(".list-item__title").get_text(strip=True) if item.select_one(".list-item__title") else None
    link = item.select_one("a")['href'] if item.select_one("a") else None
    if title and link:
        news_items.append({"title": title, "link": link})

if news_items:
    df = pd.DataFrame(news_items)
    df.to_csv(CSV_PATH, index=False)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("news", conn, if_exists="replace", index=False)
    conn.close()

print(f"Saved {len(news_items)} news items.")
