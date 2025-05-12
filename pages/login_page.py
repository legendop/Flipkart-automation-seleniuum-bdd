from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_site(self):
        self.driver.get("https://www.flipkart.com")

    def login(self, phone_number):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "H6-NpN._3N4_BX")))
        login_btn.click()

        phone_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')))
        phone_input.clear()
        phone_input.send_keys(phone_number + Keys.ENTER)

        print("Waiting for OTP...")
        time.sleep(20)  # Manual OTP entry
