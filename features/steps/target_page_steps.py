from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/CartLink']").click()

@then('Verify “Cart is Empty” message is shown')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 fJliSz']")

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'#account-sign-in').click()

@then('Click Sign In from Navigation Menu')
def nav_sign_in(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text

    assert expected_result in actual_result