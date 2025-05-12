from behave import given, when, then
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.driver_setup import init_driver
import time

@given('the user opens the Flipkart website')
def step_open_flipkart(context):
    context.driver = init_driver()
    context.login = LoginPage(context.driver)
    context.login.open_site()

@when('the user logs in with the phone number')
def step_login(context):
    context.login.login("9933212411")

@when('the user searches for "{query}"')
def step_search_product(context, query):
    context.search = SearchPage(context.driver)
    context.search.search_product(query)

@when('filters the results by brand "{brand}"')
def step_filter_brand(context, brand):
    context.search.filter_brand(brand)

@when('clicks on the first product')
def step_click_first_product(context):
    context.product = ProductPage(context.driver)
    context.product.click_first_product()

@when('selects a delivery address')
def step_enter_delivery(context):
    context.checkout = CheckoutPage(context.driver)
    context.checkout.enter_delivery_address()

@when('proceeds to the payment page')
def step_proceed_payment(context):
    context.checkout.proceed_to_payment()

@then('the user enters card details and completes payment')
def step_enter_payment(context):
    context.checkout.enter_card_details("123456781234", "02/33", "123")
    time.sleep(5)
    context.driver.quit()
