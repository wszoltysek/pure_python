import requests
from bs4 import BeautifulSoup
import json


class MovieScraper:
    """
    Module responsible for scraping TOP25 movies from Filmweb ranking page
    and save it to the json file.
    """

    @staticmethod
    def page_parser():
        url = "https://www.filmweb.pl/ranking/film"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        body = soup.body
        return body

    @staticmethod
    def content_scraper():
        positions = MovieScraper.page_parser().find_all("div", {"class": "ranking__position"})
        titles = MovieScraper.page_parser().find_all("a", {"class": "film__link"})

        pos_txt = [pos.text for pos in positions]
        title_txt = [title.text for title in titles]

        movies_dict = {k: v for k, v in zip(pos_txt, title_txt)}
        with open("movies.json", "w") as file:
            json.dump(movies_dict, file)


if __name__ == "__main__":
    MovieScraper.content_scraper()
