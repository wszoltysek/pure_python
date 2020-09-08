from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.olx.pl/")

# Wait 5 sec to load page.
time.sleep(5)

# Click cookies accept button
cookies_accept = driver.find_element_by_id("onetrust-accept-btn-handler")
if cookies_accept is not None:
    cookies_accept.click()

# Search box
search_box = driver.find_element_by_id("headerSearch")
search_box.send_keys("Yamaha WR")
search_button = driver.find_element_by_id("submit-searchmain").click()

# Wait 5 sec to load page.
time.sleep(5)

# while True:
#     try:
#         bikes = driver.find_elements_by_class_name("wrap")
#         # Bike names:
#         bike_name_list = [bike.find_element_by_tag_name("strong").text for bike in bikes]
#         # Bike links:
#         bike_links = [bike.find_element_by_tag_name("a").get_attribute("href") for bike in bikes]
#         # Bike prices:
#         bike_prices = [bike.find_element_by_class_name("price").text for bike in bikes]


# driver.find_element_by_class_name("wrapper").find_element_by_class_name("pager rel clr")


# driver.quit()
