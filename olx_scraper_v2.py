# import requests
from bs4 import BeautifulSoup
import grequests


class Scrapper:
    def __init__(self, query: str):
        self.query = query.replace(' ', '-')
        self.query_url = 'https://www.olx.pl/oferty/q-{}/'
        self.page_count = 0

    def get_page_count(self):
        r = grequests.map([grequests.get(self.query_url.format(self.query))])
        soup = BeautifulSoup(r[0].content, 'lxml')
        counter_last = soup.find_all('a', {"class": "block br3 brc8 large tdnone lheight24"})
        self.page_count = int(counter_last[-1].text)

    def get_all_by_asyncs(self):
        urls = [self.query_url.format(self.query) + '?page={}'.format(i) for i in range(self.page_count)]
        rs = (grequests.get(u) for u in urls)
        self.scrapped_pages = grequests.map(rs)

    def scrap_offers_from_page(self):
        for page in self.scrapped_pages:
            soup = BeautifulSoup(page.content, 'lxml')
            offers = soup.find_all('tr', {"class": "wrap"})
            for offer in offers:
                title = str(offer.find('h3', {"class": "lheight22 margintop5"}).text).strip()
                link = str(offer.find('a', href=True)['href'])
                price = str(offer.find('p', {"class": "price"}).text).strip()
                print('*' * 25 + '\n' + title + "\n" + link + '\n' + price)

    def run(self):
        self.get_page_count()
        self.get_all_by_asyncs()
        self.scrap_offers_from_page()


olx_scrapper = Scrapper('Yamaha WR')
olx_scrapper.run()

# python3 olx.py 4.61 sekund :)
# Przy uzyciu async requests z gevent
