import requests
from bs4 import BeautifulSoup
import json


class MovieScraper:
    """
    Module responsible for scraping TOP25 movies from Filmweb ranking page
    and save it to the json file.
    """

    def __init__(self):
        self.url = "https://www.filmweb.pl/ranking/film"

    def page_parser(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "lxml")
        self.body = soup.body

    def content_scraper(self):
        positions = self.body.find_all("div", {"class": "ranking__position"})
        titles = self.body.find_all("a", {"class": "film__link"})

        pos_txt = [pos.text for pos in positions]
        title_txt = [title.text for title in titles]

        movies_dict = {k: v for k, v in zip(pos_txt, title_txt)}
        with open("movies.json", "w") as file:
            json.dump(movies_dict, file)

    def run(self):
        self.page_parser()
        self.content_scraper()


if __name__ == "__main__":
    ms = MovieScraper()
    ms.run()
