import unittest
import json
import sys
import os

sys.path.append("../")
from filmweb_scraper import MovieScraper


class TestMovieScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_content = MovieScraper.page_parser()

    def test_page_content_exists(self):
        self.assertIsNotNone(self.page_content)

    def test_movie_positions(self):
        positions = self.page_content.find_all("div", {"class": "ranking__position"})
        self.assertIsNotNone(positions)
        self.assertIsInstance(positions, list)

    def test_movie_titles(self):
        titles = self.page_content.find_all("a", {"class": "film__link"})
        self.assertIsNotNone(titles)
        self.assertIsInstance(titles, list)

    def test_saving_to_json(self):
        sample_json = {
            "1": "Movie",
            "2": "Another Movie",
            "3": "Third Movie"
        }
        with open("movies.json", "w") as save_file:
            json.dump(sample_json, save_file)
        self.assertIsNotNone(save_file)

        with open("movies.json") as read_file:
            data = json.load(read_file)
        self.assertEqual(data, sample_json)

    @classmethod
    def tearDownClass(cls):
        os.remove("movies.json")


if __name__ == '__main__':
    unittest.main()
