import requests
from bs4 import BeautifulSoup
# lxml - the fastest parser for html.


class MovieScraper:
    """
    Module responsible for scraping TOP movies from Filmweb page ranking
    and save it to the database.
    """

    @staticmethod
    def scrap_movies():
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


if __name__ == "__main__":
    MovieScraper.scrap_movies()

"""
TODO:
- wyszukanie wszystkich
- program obiektowo z metodami.
    - metoda 1 do otwiernia, metoda 2 do pobiernia, metoda 3 do zapisu
- zapisywanie do bazy danych

"""
