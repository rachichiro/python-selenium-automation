from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SignInPage(BasePage):

 SIGN_INTO_ACCT_MSG = (By.XPATH, "//*[text()='Sign into your Target account']")
 TNC_BTN = (By.CSS_SELECTOR, "a[href='/c/terms-conditions/-/N-4sr7l']")


 #def verify_sign_in(self):
 #self.verify_text(*self.SIGN_INTO_ACCT_MSG).text
 def verify_sign_in(self):
    WebDriverWait(self.driver, 10).until(
       EC.visibility_of_element_located(self.SIGN_INTO_ACCT_MSG))

 def open_signin(self):
     self.open_url('https://www.target.com/account?prehydrateClick=true')

 def click_tnc(self):
  self.driver.find_element(*self.TNC_BTN).click()
