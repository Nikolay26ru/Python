import pytest
import os
import sqlite3

def test_scraper_creates_db():
    if os.path.exists("news.db"):
        os.remove("news.db")
    import scraper
    assert os.path.exists("news.db")
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM news")
    assert c.fetchone()[0] > 0
    conn.close()
