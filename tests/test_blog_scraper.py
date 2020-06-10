import csv
import unittest
import sys
import os

sys.path.append("../")
from blog_scraper import BlogScraper


class TestBlogScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.page = BlogScraper.page_parser()

    def test_page_exists(self):
        self.assertIsNotNone(self.page)

    def test_content(self):
        content = self.page.find("div", {"class": "wpb_column vc_column_container vc_col-sm-8"})
        articles = content.find("div", {"class": "row"}).find_all("article")
        self.assertIsNotNone(content)
        self.assertIsNotNone(articles)
        self.assertIsInstance(articles, list)

    def test_saving_to_csv_file(self):
        with open("blog_content.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["title", "date", "summary", "link"])
        self.assertIsNotNone(csv_file)

    def test_csv_file_content(self):
        sample_content_list = ["title", "date", "summary", "link"]
        sample_content_ok = "title,date,summary,link\n"

        with open("blog_content.csv") as csv_file:
            file_content = csv_file.read()

        self.assertNotEqual(file_content, sample_content_list)
        self.assertEqual(file_content, sample_content_ok)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove("blog_content.csv")


if __name__ == '__main__':
    unittest.main()
