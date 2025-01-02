# Created by rachael at 12/27/24
Feature: Verify that a logged out user can access sign in

  Scenario:
    Given Open Target Page
    When Click Sign In
    Then Click Sign In from Navigation Menu
    Then Verify Sign In form opened