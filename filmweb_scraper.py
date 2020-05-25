import requests
from bs4 import BeautifulSoup
# lxml - najszybszy parser html


url = "https://www.filmweb.pl/ranking/film"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
body = soup.body


positions = body.find_all("div", {"class": "ranking__position"})
titles = body.find_all("a", {"class": "film__link"})

pos_txt = [pos.text for pos in positions]
title_txt = [title.text for title in titles]


movies_dict = {k: v for k, v in zip(pos_txt, title_txt)}
for k, v in movies_dict.items():
    print(f"Pozycja: {k}, Tytuł: {v}")


"""
TODO:
- wyszukanie wszystkich
- program obiektowo z metodami
- zapisywanie do bazy danych

"""
