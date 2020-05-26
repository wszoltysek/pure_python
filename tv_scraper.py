import requests
from bs4 import BeautifulSoup
import re


class TVScraper:

    @staticmethod
    def page_parser():
        url = "https://www.teleman.pl/program-tv?hour=20"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        page_body = soup.body
        return page_body

    @staticmethod
    def page_content_scraper():

        # NAZWY WSZYSTKICH KANAŁÓW TV:
        # tv_stations = TVScraper.page_parser().find_all("div", {"class": "name"})
        # tv_stations_txt: str = [station.text for station in tv_stations]
        # print(tv_stations_txt)

        # POLSAT:
        polsat = TVScraper.page_parser().find("div", {"data-station-id": "3"})
        polsat_name = polsat.find("div", {"class": "name"})
        first_show = polsat.find("a", {"class": "prog-title"})
        # first_show_hour = first_show.attrs["data-time"]
        first_show_hour = polsat.find("span", {"class": "time"})

        print(polsat_name.text) # Polsat
        print(first_show.text) # Dzień Matki
        print(first_show_hour.text) # 20:00


if __name__ == "__main__":
    TVScraper.page_content_scraper()



# time = TVScraper.page_parser()("span", {"class": "time"})
# time_txt: str = [time.text for time in time]
# time_str = (" ".join(time_txt))
# searched_hour = re.findall(r"(1[2]|2[0]:[0-5][0-9])", time_str)
# print(searched_hour)

# tv_dict = {k: v for k, v in zip(titles_txt, searched_hour)}
# for k, v in tv_dict.items():
#     print(k, v)


"""
ZAMYSŁ: 
- Stacja: TVN Tytuł: Nazwa Godzina: 20:00+
- Programy na stronie rozpoczynające się po 20:00, zatem regex też musi wyszukiwać od 20:00 do 24:00
- Stacja, Titles i times musza byc tak pobierane zeby razem byly powiazane jakos.
- Dopiero wtedy mozna je razem zapisac (np. do dict)

- lista jako kolumna w sql lite - zapis !
- nazwa programu i jego godzina musza byc razem
- dopisz kolumne date z date.today przy zapisie

"""
