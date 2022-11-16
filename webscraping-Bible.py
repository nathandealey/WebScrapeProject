import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'
#website is crashed + absent

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll("div", class_ = "min")

print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split(".")

#sprint(verse_list)

myverse = random.choice(verse_list)

print(myverse)

