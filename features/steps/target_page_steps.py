from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID,'search')
SEARCH_BUTTON = (By.XPATH,"//button[@data-test='@web/Search/SearchButton']")


@then('Click Sign In from Navigation Menu')
def nav_sign_in(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text

    assert expected_result in actual_result


@then('Verify search results show {expected_result}')
def verify_search(context,expected_result):
   context.app.search_results_page.verify_search_results()