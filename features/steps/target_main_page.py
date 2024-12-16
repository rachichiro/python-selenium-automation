from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



@given('Open Target Page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'#account-sign-in').click()

@when('Click on Cart Icon')
def click_cart_icon(context):
     context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


