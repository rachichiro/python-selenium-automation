# Created by rachael at 12/9/24
Feature: Tests for Product Search

  Scenario: User can search for tea
    Given Open Target Page
    When Search for tea
    Then Verify search results show tea

  Scenario: User can search for coca cola
    Given Open Target Page
    When Search for coca cola
    Then Verify search results show coca cola

  Scenario: User can search for a mug
    Given Open Target Page
    When Search for mug
    Then Verify search results show mug

  Scenario Outline: User can search for a product
    Given Open Target Page
    When Search for <product>
    Then Verify search results show <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |