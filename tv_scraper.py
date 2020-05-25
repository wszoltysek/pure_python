import requests
from bs4 import BeautifulSoup
import re

url = "https://www.teleman.pl/program-tv?hour=20"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
page_body = soup.body


titles = page_body("a", {"class": "prog-title"})
titles_txt = [title.text for title in titles]
# for title in titles_txt:
#     print(title)


time = page_body("span", {"class": "time"})
time_txt: str = [time.text for time in time]
time_str = (" ".join(time_txt))

searched_hour = re.findall(r"(1[2]|2[0]:[0-5][0-9])", time_str)
print(searched_hour)


# for t in time_str:
#     if t in searched_hour:
#         print(t)
# #
# # result = [t for t in yield_20_our(time_txt)]
