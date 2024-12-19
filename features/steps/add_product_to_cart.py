from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


#ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[data-test='orderPickupButton'][id*='addToCartButton']")
VIEW_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[href='/cart']")
PRODUCT_NAME = (By.CSS_SELECTOR,"[data-test='content-wrapper'] h4")

@when ('Open Cart Page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@then ('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then ('Add product to cart')
def add_product_to_cart(context):
    context.app.cart_page.add_product_to_cart()

@then ('Confirm add to cart from Side Nav')
def confirm_add_to_cart(context):
 context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()


@then ('Verify product is in cart')
def verify_add_to_cart(context):
    context.driver.find_element(*VIEW_CART_SIDE_NAV_BTN).click()
    expected_result = '1 item'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='1 item']").text

    assert expected_result in actual_result, f'Expected: {expected_result} but got  Actual: {actual_result}'

@then ('Store Product Name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')

@then ('Verify correct product in Cart')
def verify_product_name(context):
    actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(f'Actual product in cart name: {actual_name}')
    print(f'Product name stored earlier: {context.product_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify “Cart is Empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

