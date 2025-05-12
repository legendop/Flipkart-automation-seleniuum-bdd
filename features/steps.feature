Feature: Flipkart Purchase Flow

  Scenario: User searches and proceeds to payment for a Puma shoe
    Given the user opens the Flipkart website
    When the user logs in with the phone number
    And the user searches for "shoes men"
    And filters the results by brand "Puma"
    And clicks on the first product
    And selects a delivery address
    And proceeds to the payment page
    Then the user enters card details and completes payment
