import requests
from bs4 import BeautifulSoup
import unittest
# from tv_scraper import TVScraper


class TestTVScraper(unittest.TestCase):

    def setUp(self):
        url = "https://www.teleman.pl/program-tv/stacje/TVN?hour=-1"
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "lxml")

    def test_station_title(self):
        title = self.soup.find("h1").text
        self.assertEqual(title, "TVN")

    def test_content_exists(self):
        content = self.soup
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()
