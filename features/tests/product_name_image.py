from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

PRODUCTS= (By.XPATH,"//a[@data-test='product-title']")

@then ('Verify each product has an image and name')
def verify_name_img(context):
    products = context.driver.find_elements(*PRODUCTS)

    for product in products:
        selected_product = context.driver.find_elements(*PRODUCTS).text
        print(selected_product)