from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[id*='addToCartButton']")


    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        self.verify_text(expected_result,*self.CART_EMPTY_MSG)

    def add_product_to_cart(self):
        sleep(10)
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()