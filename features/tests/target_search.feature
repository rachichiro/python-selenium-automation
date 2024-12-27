# Created by rachael at 12/9/24
Feature: Tests for Product Search

  Scenario: User can search for tea
    Given Open Target Page
    When Search for tea
    Then Verify search results show tea
    Then Verify search term tea in URL

  Scenario: User can search for soda
    Given Open Target Page
    When Search for soda
    Then Verify search results show soda
    Then Verify search term soda in URL

  Scenario: User can search for a mug
    Given Open Target Page
    When Search for mug
    Then Verify search results show mug
    Then Verify search term mug in URL

  Scenario Outline: User can search for a product
    Given Open Target Page
    When Search for <product>
    Then Verify search results show <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |