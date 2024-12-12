# Created by rachael at 12/11/24
Feature: Ensure user can add products to cart

  Scenario: Add products to cart
  Given  Open Target Page
  When Search for ginger ale
  Then Add product to cart
  Then Confirm add to cart
  Then Verify product is in cart