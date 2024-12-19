from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service

#CART_ICON = (By.CSS_SELECTOR,"[@data-test='@web/CartLink']")

@given('Open Target Page')
def open_target(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context,product):
   context.app.header.search_products(product)

@when('Click Sign In')
def click_sign_in(context):
    #context.driver.find_element(By.CSS_SELECTOR,'#account-sign-in').click()
    context.app.header.click_sign_in()

@when('Click on Cart Icon')
def click_cart(context):
     context.app.header.click_cart()


@then('Verify at least 1 Header Link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'