# Created by rachael at 12/9/24
Feature: Tests for Product Search

  Scenario: User can search for ginger ale
    Given Open Target Page
    When Search for ginger ale
    Then Verify search results show ginger ale

  Scenario: User can search for coca cola
    Given Open Target Page
    When Search for coca cola
    Then Verify search results show coca cola