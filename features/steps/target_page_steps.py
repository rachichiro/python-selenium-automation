from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH,"//button[@data-test='@web/Search/SearchButton']")



@then('Verify “Cart is Empty” message is shown')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 fJliSz']")


@then('Click Sign In from Navigation Menu')
def nav_sign_in(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text

    assert expected_result in actual_result

@when('Search for {drink}')
def search_drink(context,drink):
    context.driver.find_element(*SEARCH_FIELD).send_keys(drink)
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Verify search results show {expected_result}')
def verify_search(context,expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result,f'Expected text{expected_result} but got {actual_result}'