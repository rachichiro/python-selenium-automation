from pages.header import Header
from pages.cart_page import CartPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.side_nav_page import SideNavPage
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.terms_condtions_page import TermsConditionsPage


class Application:

    def __init__(self,driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.side_nav_page = SideNavPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)