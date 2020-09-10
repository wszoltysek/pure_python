import requests
from bs4 import BeautifulSoup
import csv


class BlogScraper:
    """
       Module responsible for scraping posts content from event blog
       by title, date, summary, link and save it to the csv file.
    """

    def __init__(self):
        self.url = "https://eventowablogerka.pl/"

    def load_page(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "lxml")
        self.page_body = soup.body

    def content_scraper(self):
        content = self.page_body.find("div", {"class": "wpb_column vc_column_container vc_col-sm-8"})
        articles = content.find("div", {"class": "row"}).find_all("article")

        with open("blog_content.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["title", "date", "summary", "link"])

            for single_art in articles:
                title = single_art.h2.text
                date = single_art.li["datetime"]
                delete_a = single_art.find("a", {"class": "continue-reading"}).decompose()
                summary = single_art.p.text
                link = single_art.a["href"]

                csv_writer.writerow([title, date, summary, link])

    def run(self):
        self.load_page()
        self.content_scraper()


if __name__ == "__main__":
    bs = BlogScraper()
    bs.run()
