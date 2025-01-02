

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class TermsConditionsPage(BasePage):

    TNC_MSG = (By.XPATH, "//*[text()='Terms & Conditions']" )

    def verify_tnc_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TNC_MSG))