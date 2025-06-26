import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
# proxies = {'https': 'http://165.225.72.38:10211/'}


def get_info(id: str):
    dotabuff = "https://www.dotabuff.com/players/" + id
    response = requests.get(dotabuff, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="header-content-secondary")
    w = data.find_all('dl')
    return w[-1].text

