
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID,'search')
    SEARCH_BUTTON = (By.XPATH,"//button[@aria-label='search']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.CSS_SELECTOR,'#account-sign-in')

    def search_products(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart(self):
     #self.click(*self.CART_ICON)
     self.wait_and_click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)