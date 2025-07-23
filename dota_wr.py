import requests
import cloudscraper
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.google.com/",
}
# proxies = {'https': '172.66.46.244:443'}

def get_info(id: str):
    dotabuff = "https://www.dotabuff.com/players/" + id
    scraper = cloudscraper.create_scraper()
    response = scraper.get(dotabuff, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="header-content-secondary")
    w = data.find_all('dl')
    return w[-1].text

