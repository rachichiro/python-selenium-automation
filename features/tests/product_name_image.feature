Feature: Tests for Product Image & Image

  Scenario: Verify every product on search results page has image and name
    Given Open Target Page
    When Search for lemonade
    Then Verify each product has an image and name