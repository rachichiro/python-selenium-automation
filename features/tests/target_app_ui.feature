# Created by rachael at 12/26/24
Feature:  Tests for Target App Page

  Scenario:
    Given Open Target App Page
    Then Store Original Window
    When Click Privacy Policy Link
    Then Switch to New Window
    Then Verify Privacy Policy Window Opened
    And  Close Current Window
    And Return to Original Window