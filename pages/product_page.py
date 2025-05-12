from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_first_product(self):
        xpath = "//*[@id='container']/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div/div/img"
        max_retries = 5
        for attempt in range(max_retries):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                product_tile = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", product_tile)
                time.sleep(1)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                product_tile.click()
                print("Product tile clicked successfully.")
                break
            except (StaleElementReferenceException, TimeoutException):
                print(f"[Attempt {attempt+1}] Retrying click on product...")
                time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
