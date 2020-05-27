import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3


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
        hours_list = [hour.text for hour in hours if len(hour.text) > 1]

        # Shows details:
        shows_details = TVScraper.page_parser().find_all("div", {"class": "detail"})
        shows_name_list = [name.text for a in shows_details
                           for name in a.find_all("a") if len(name.text) > 1]
        shows_genre_list = [desc.text for p in shows_details
                            for desc in p.find_all("p", {"class": "genre"}) if len(desc.text) > 1]

        # Date:
        date = datetime.date.today()

        # Saving to database:
        conn = sqlite3.connect("tv.sqlite")
        cursor = conn.cursor()

        conn.execute('''CREATE TABLE IF NOT EXISTS tv_shows
                     (time integer NOT NULL,
                     name text NOT NULL,
                     description text NOT NULL,
                     date date NOT NULL
                     );''')

        for h, n, g in zip(hours_list, shows_name_list, shows_genre_list):
            cursor.execute("INSERT INTO tv_shows VALUES (?, ?, ?, ?)", (h, n, g, date))
            conn.commit()

        # Printing saved content in terminal:

        # fmt = "{:<10}{:<35}{}"
        # print(f"STACJA: {station_name}")
        # print(f"Data programu: {datetime.date.today()}\n")
        # print(fmt.format("GODZINA", "PROGRAM", "OPIS"))
        # for h, n, g in zip(hours_list, shows_name_list, shows_genre_list):
        #     print(fmt.format(h, n, g))


if __name__ == "__main__":
    TVScraper.page_content_scraper()


"""
ZAMYSŁ: 
- docstring
"""


