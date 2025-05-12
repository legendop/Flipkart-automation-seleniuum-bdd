# Flipkart Automation using Selenium BDD Python

This project automates the Flipkart login, search, filter, product selection, and payment flow using Selenium WebDriver with Python's Behavior-Driven Development (BDD) approach. The automation script simulates the following actions:

1. Login to Flipkart using a phone number (manual OTP entry required).
2. Search for shoes and filter results for Puma shoes.
3. Select the first product in the search results.
4. Open the product page in a new tab.
5. Switch to the new tab and click the "Buy Now" button.
6. Enter fake card details and simulate a payment.

## Project Setup

### Setup Instructions

1. **Clone the repository:**

    If you haven't already cloned the repository, run:

    ```bash
    git clone https://github.com/legendop/Flipkart-Automation-Selenium-BDD.git
    cd Flipkart-Automation-Selenium-BDD
    ```

2. **Install the required dependencies:**

    Run the following command to install all necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file:**

    In the project root directory (`FLIPKART_AUTOMATION_BDD`), create a `.env` file and add it with your phone number and card details:

    ```bash
    PHONE_NUMBER=1234567890
    CARD_NUMBER=123123123123
    CARD_EXPIRY=10/32
    CARD_CVV=111
    ```

4. **Run:**


    ```bash
    behave
    ```