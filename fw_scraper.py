from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


class FWScraper:

    def __init__(self):
        self.url = "https://www.filmweb.pl/ranking/film"

    def get_page(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(5)
        driver.find_element_by_class_name("ws__skipButton").click()
        driver.find_element_by_id("didomi-notice-agree-button").click()
        driver.execute_script("window.scrollTo(0, 500)")
        # html = driver.page_source
        # self.soup = BeautifulSoup(html, "lxml")

    def scrape_elements(self):
        positions = self.soup.find_all("div", {"class": "ranking__position"})
        titles = self.soup.find_all("a", {"class": "film__link"})

        pos_txt = [pos.text for pos in positions]
        title_txt = [title.text for title in titles]

        movies_dict = {k: v for k, v in zip(pos_txt, title_txt)}
        print(movies_dict)

        # with open("movies.json", "w") as file:
        #     json.dump(movies_dict, file)

    def run(self):
        self.get_page()
        # self.scrape_elements()


fw = FWScraper()
fw.run()
