# Created by rachael at 12/7/24
Feature: Target Page Tests
  Check different functions and buttons on Target page.

  Scenario: Verify shopping cart is empty
    Given Open Target Page
    When Click on Cart Icon
    Then Verify “Cart is Empty” message is shown

  Scenario: Verify that a logged out user can navigate to Sign In
   Given Open Target Page
   When Click Sign In
   Then Click Sign In from Navigation Menu
   Then Verify Sign In form opened
