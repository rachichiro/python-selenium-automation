# Created by rachael at 1/2/25
Feature: Terms & Condition Open

   Scenario: User can open and close Terms and Conditions from sign in page
     Given Open Target Page
   When Click Sign In
   Then Click Sign In from Navigation Menu
     When Store Original Window
 Then Click on Terms & Conditions Link
 Then Switch to the New Window
 Then Verify Terms and Conditions Page Opened
     Then Close New Window
 Then Return to Original Window