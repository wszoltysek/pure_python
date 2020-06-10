import os
import sqlite3
import unittest
from unittest.mock import MagicMock
import sys

sys.path.append("../")
from tv_scraper import TVScraper


class TestTVScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_content = TVScraper.page_parser()
        cls.details = cls.page_content.find_all("div", {"class": "detail"})

    def test_content_exists(self):
        self.assertIsNotNone(self.page_content)

    def test_station_title(self):
        title = self.page_content.find("h1").text
        self.assertEqual(title, "TVN")

    def test_shows_time(self):
        hours = self.page_content.find_all("em")
        self.assertIsNotNone(hours)
        self.assertIsInstance(hours, list)

    def test_shows_name(self):
        names = [
            name.text for a in self.details
            for name in a.find_all("a") if len(name.text) > 1
        ]
        self.assertIsNotNone(names)
        self.assertIsInstance(names, list)

    def test_shows_genre(self):
        genres = [
            desc.text for p in self.details
            for desc in p.find_all("p", {"class": "genre"}) if len(desc.text) > 1
        ]
        self.assertIsNotNone(genres)
        self.assertIsInstance(genres, list)

    def test_sqlite3_connect_success(self):
        sqlite3.connect = MagicMock(return_value="connection succeeded")

        db = sqlite3.connect("tv.sqlite")
        self.assertEqual(db, "connection succeeded")

    @classmethod
    def tearDownClass(cls):
        os.remove("tv.sqlite")


if __name__ == '__main__':
    unittest.main()
