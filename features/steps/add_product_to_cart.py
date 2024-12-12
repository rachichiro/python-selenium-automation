from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then ('Add product to cart')
def add_product_to_cart(context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR,"[id*='addToCartButton']").click()
    sleep(4)

@then ('Confirm add to cart')
def confirm_add_to_cart(context):
 context.driver.find_element(By.CSS_SELECTOR,"[data-test='orderPickupButton'][id*='addToCartButton']").click()


@then ('Verify product is in cart')
def verify_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()
    sleep(5)
    expected_result = '1 item'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='1 item']").text

    assert expected_result in actual_result, f'Expected: {expected_result} but got  Actual: {actual_result}'



