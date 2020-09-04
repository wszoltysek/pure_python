from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.olx.pl/")
time.sleep(5)
driver.close()
