import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3


class TVScraper:
    """
    Module responsible for scraping TV program of a specific station
    from teleman.pl page and save it to sqlite database.
    """

    def __init__(self, station: str):
        self.station = station
        self.url = f"https://www.teleman.pl/program-tv/stacje/{self.station}?hour=-1"

    def page_parser(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "lxml")
        self.page_body = soup.body

    def page_content_scraper(self):
        # Station name:
        station_name = self.page_body.find("h1").text

        # Date:
        date = datetime.date.today()

        # Shows time:
        hours = self.page_body.find_all("em")
        hours_list = [hour.text for hour in hours if len(hour.text) > 1]

        # Shows details:
        shows_details = self.page_body.find_all("div", {"class": "detail"})
        shows_name_list = [
            name.text for a in shows_details
            for name in a.find_all("a") if len(name.text) > 1
        ]
        shows_genre_list = [
            desc.text for p in shows_details
            for desc in p.find_all("p", {"class": "genre"}) if len(desc.text) > 1
        ]

        # Saving to database:
        conn = sqlite3.connect("tv.sqlite")
        cursor = conn.cursor()

        conn.execute("""CREATE TABLE IF NOT EXISTS tv_program
                     (station text NOT NULL,
                     time integer NOT NULL,
                     name text NOT NULL,
                     description text NOT NULL,
                     date date NOT NULL
                     );""")

        for h, n, g in zip(hours_list, shows_name_list, shows_genre_list):
            cursor.execute("INSERT INTO tv_program VALUES (?, ?, ?, ?, ?)",
                           (station_name, h, n, g, date))
            conn.commit()

        # Printing saved content in terminal:

        fmt = "{:<5}{:<10}{:<50}{}"
        print(f"STATION: {station_name}")
        print(f"Program date: {date}\n")
        print(fmt.format("NR", "TIME", "PROGRAM", "DESCRIPTION"))
        for i, (h, n, g) in enumerate(zip(hours_list, shows_name_list, shows_genre_list), start=1):
            print(fmt.format(i, h, n, g))
        print("\nContent saved to the database.")

    def run(self):
        self.page_parser()
        self.page_content_scraper()


if __name__ == "__main__":
    tv = TVScraper("Polsat")
    tv.run()
