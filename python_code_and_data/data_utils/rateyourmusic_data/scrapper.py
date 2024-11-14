from bs4 import BeautifulSoup
import requests
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

#url = "http://webcache.googleusercontent.com/search?q=cache:https://rateyourmusic.com/list/montezuma/all-dead-all-dead-worlds-largest-list-of-deceased-musicians/1/"


for page_number in range(1,19):
    url = f"http://webcache.googleusercontent.com/search?q=cache:https://rateyourmusic.com/list/montezuma/all-dead-all-dead-worlds-largest-list-of-deceased-musicians/{page_number}/"
    time.sleep(random.uniform(1, 20))
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    f = open(f"data/result{page_number}.txt", "w", encoding="utf-8")
    f.write(soup.prettify())
    f.close()



