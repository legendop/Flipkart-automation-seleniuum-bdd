from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def search_product(self, query):
        search_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and @title="Search for Products, Brands and More"]')))
        search_input.click()
        search_input.clear()
        search_input.send_keys(query + Keys.ENTER)

    def filter_brand(self, brand):
        brand_filter = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "XPD6hh")))
        brand_filter.send_keys(brand)
        puma_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[5]/div[2]/div[1]/div[2]/div/label/div[1]")))
        puma_checkbox.click()
        time.sleep(3)
