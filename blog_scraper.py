import requests
from bs4 import BeautifulSoup
import csv


class BlogScraper:
    """
    Module responsible for scraping posts content from event blog
    by title, date, summary, link and save it to the csv file.
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

        with open("blog_content.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["title", "date", "summary", "link"])

            for single_art in articles:
                title = single_art.h2.text
                date = single_art.li["datetime"]
                main_summary = single_art.p
                delete_a = single_art.find("a", {"class": "continue-reading"}).decompose()
                summary = main_summary.text
                link = single_art.a["href"]

                csv_writer.writerow([title, date, summary, link])


if __name__ == "__main__":
    BlogScraper.content_scraper()
