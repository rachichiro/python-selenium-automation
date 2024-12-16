from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[data-test='orderPickupButton'][id*='addToCartButton']")
VIEW_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[href='/cart']")

@then ('Add product to cart')
def add_product_to_cart(context):
    sleep(10)
    #context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN)).click()
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@then ('Confirm add to cart')
def confirm_add_to_cart(context):
 context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()


@then ('Verify product is in cart')
def verify_add_to_cart(context):
    context.driver.find_element(*VIEW_CART_SIDE_NAV_BTN).click()
    expected_result = '1 item'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='1 item']").text

    assert expected_result in actual_result, f'Expected: {expected_result} but got  Actual: {actual_result}'



