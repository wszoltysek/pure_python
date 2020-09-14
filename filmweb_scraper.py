import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


class FWScraper:
    """
    Module responsible for scraping TOP500 movies from Filmweb ranking page
    and save it to the json file.
    """

    def __init__(self):
        self.url = "https://www.filmweb.pl/ranking/film"

    def get_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(5)
        try:
            self.driver.find_element_by_class_name("ws__skipButton")
        except selenium.common.exceptions.NoSuchElementException:
            pass
        self.driver.find_element_by_id("didomi-notice-agree-button").click()

    def page_content(self):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "lxml")

    def scrape_elements(self):
        scroll_down = 1000
        memory = []
        index = 0

        while True:
            self.page_content()
            self.driver.execute_script(f"window.scrollTo(0,{scroll_down})")
            positions = self.soup.find_all("span", {"class": "film__position"})
            titles = self.soup.find_all("a", {"class": "film__link"})
            pos_int = [int(pos.text.replace(".", "")) for pos in positions]
            title_txt = [title.text for title in titles]
            print(pos_int)

            if len(pos_int) >= len(memory):
                if pos_int == memory:
                    index += 1
                memory = pos_int
                if index == 5:
                    scroll_down -= 200
                if 500 in pos_int:
                    break
                scroll_down += 100

        movies_dict = {k: v for k, v in zip(pos_int, title_txt)}
        print(movies_dict)

        with open("movies.json", "w") as file:
            json.dump(movies_dict, file)

    def run(self):
        self.get_page()
        self.scrape_elements()


fw = FWScraper()
fw.run()
