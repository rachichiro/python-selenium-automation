# Created by rachael at 12/18/24
Feature: Tests for Main Page UI

  Scenario: User can see Header Links
    Given Open Target Page
    Then Verify at least 1 Header Link is shown

  Scenario: User can see correct amount of Header Links
    Given Open Target Page
    Then Verify 6 Header Links are shown