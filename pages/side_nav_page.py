from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SideNavPage(BasePage):
    SIGN_IN_BTN = (By.XPATH,"//button[@data-test='accountNav-signIn']")

    def nav_sign_in(self):
       self.driver.find_element(*self.SIGN_IN_BTN).click()