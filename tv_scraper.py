import requests
from bs4 import BeautifulSoup
import re

url = "https://www.teleman.pl/program-tv?hour=20"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
page_body = soup.body


titles = page_body("a", {"class": "prog-title"})
titles_txt = [title.text for title in titles]


time = page_body("span", {"class": "time"})
time_txt: str = [time.text for time in time]
time_str = (" ".join(time_txt))

searched_hour = re.findall(r"(1[2]|2[0]:[0-5][0-9])", time_str)
# print(searched_hour)

tv_dict = {k: v for k, v in zip(titles_txt, searched_hour)}
for k, v in tv_dict.items():
    print(k, v)


"""
ZAMYSŁ: 
- Stacja: TVN Tytuł: Nazwa Godzina: 20:00+
- Programy na stronie rozpoczynające się po 20:00, zatem regex też musi wyszukiwać od 20:00 do 24:00
- Stacja, Titles i times musza byc tak pobierane zeby razem byly powiazane jakos.
- Dopiero wtedy mozna je razem zapisac (np. do dict)

"""
