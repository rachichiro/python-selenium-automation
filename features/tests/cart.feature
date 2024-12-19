# Created by rachael at 12/11/24
Feature: Test Cart Functionality

  Scenario: Verify shopping cart is empty
    Given Open Target Page
    When Click on Cart Icon
    Then Verify “Cart is Empty” message is shown


  Scenario: Add products to cart
    Given Open Target Page
    When Search for ginger ale
    Then Add product to cart
    And Store Product Name
    Then Confirm add to cart from Side Nav
    Then Verify product is in cart
    And Verify correct product in Cart