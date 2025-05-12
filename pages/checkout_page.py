from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_delivery_address(self):
        pincode_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")))
        pincode_button.click()
        time.sleep(2)

    def proceed_to_payment(self):
        pay_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "to-payment")))
        pay_btn.click()
        time.sleep(5)

    def enter_card_details(self, number, expiry, cvv):
        self.driver.find_element(By.XPATH, "//*[@id='container']/div[2]/div/section[1]/div/div/div/section/div/div[3]/div[1]/div").click()
        card_input = self.wait.until(EC.element_to_be_clickable((By.ID, "cc-input")))
        card_input.send_keys(number)
        self.driver.find_element(By.XPATH, "//*[@id='cards']/div/div[2]/div[1]/input").send_keys(expiry)
        self.driver.find_element(By.ID, "cvv-input").send_keys(cvv)
        self.driver.find_element(By.XPATH, "//*[@id='cards']/div/button").click()
