import requests
from bs4 import BeautifulSoup


class BlogScraper:
    """
    To be added.
    """

    @staticmethod
    def page_parser():
        url = "https://eventowablogerka.pl/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        page_body = soup.body
        return page_body

    @staticmethod
    def content_scraper():
        page = BlogScraper.page_parser()
        content = page.find("div", {"class": "wpb_column vc_column_container vc_col-sm-8"})
        articles = content.find("div", {"class": "row"}).find_all("article")

        for single_art in articles:
            titles = single_art.h2.text
            date = single_art.li["datetime"]
            summary = single_art.p.text
            link = single_art.a["href"]


if __name__ == "__main__":
    BlogScraper.content_scraper()
