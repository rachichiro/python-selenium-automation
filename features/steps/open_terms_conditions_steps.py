from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

#@given ('Open Target Sign In Page')
#def open_signin(context):
    #context.app.sign_in_page.open_signin()

@when ('Store Original Window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    sleep(3)

@then ('Click on Terms & Conditions Link')
def click_tnc(context):
    context.app.sign_in_page.click_tnc()
    sleep(3)

@then('Switch to the New Window')
def switch_window(context):
    context.app.base_page.switch_to_window()
    sleep(4)

@then('Verify Terms and Conditions Page Opened')
def verify_tnc_page(context):
    context.app.terms_conditions_page.verify_tnc_page()

@then('Close New Window')
def close_page(context):
    context.app.base_page.close_window()

@then('Return to Original Window')
def return_to_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)