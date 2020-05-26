import requests
from bs4 import BeautifulSoup
import re


class TVScraper:

    @staticmethod
    def page_parser():
        url = "https://www.teleman.pl/program-tv/stacje/Polsat?hour=-1"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        page_body = soup.body
        return page_body

    @staticmethod
    def page_content_scraper():
        # Station name:
        station_name = TVScraper.page_parser().find("h1").text

        # Shows time:
        hours = TVScraper.page_parser().find_all("em")
        hours_list = [hour.text for hour in hours]

        # Shows details:
        shows_details = TVScraper.page_parser().find_all("div", {"class": "detail"})
        shows_name_list = [name.text for a in shows_details for name in a.find_all("a") if len(name.text) > 1]
        shows_genre_list = [desc.text for p in shows_details for desc in p.find_all("p", {"class": "genre"})]

        for h, n, g in zip(hours_list, shows_name_list, shows_genre_list):
            print(f"Godzina: {h}, Program: {n}, Opis: {g}")


if __name__ == "__main__":
    TVScraper.page_content_scraper()



"""
ZAMYSŁ: 
- Print Nazwa stacji: <nazwa>
- Print Data programu: Date.today
- Print (dane zapisane)
- lista jako kolumna w sql lite - zapis !
- trzecia lista to opis
- dopisz kolumne date z date.today przy zapisie
- docstring

"""
