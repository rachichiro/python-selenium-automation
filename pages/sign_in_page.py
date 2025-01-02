from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SignInPage(BasePage):

 SIGN_INTO_ACCT_MSG = (By.XPATH, "//*[text()='Sign into your Target account']")

 #def verify_sign_in(self):
 #self.verify_text(*self.SIGN_INTO_ACCT_MSG).text
 def verify_sign_in(self):
    WebDriverWait(self.driver, 10).until(
       EC.visibility_of_element_located(self.SIGN_INTO_ACCT_MSG))