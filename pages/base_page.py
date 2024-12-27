from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self,url):
        return self.driver.current_url

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_visible(self, *locator):
       return self.wait.until(EC.visibility_of_element_located(locator),
       message = f'Element by {locator} was not visible.'
                        )

    def wait_for_element_invisible(self, *locator):
        self.wait.until(EC.invisibility_of_element_located(locator),
       message = f'Element by {locator} should not be visible.'
                        )

    def wait_for_element_clickable(self,*locator):
       return self.wait.until(EC.element_to_be_clickable(locator),
                        message = f'Element by {locator} was not clickable.'
                        )

    def wait_and_click(self,*locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message = f'Element by {locator} was not clickable.'
                        ).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    def verify_partial_url(self, expected_url):
        url = self.driver.current_url
        assert expected_url in url, f'Expected partial URL {expected_url} not in  {url}'

    def verify_url(self, expected_url):
        url = self.driver.current_url
        assert expected_url == url, f'Expected URL {expected_url} does not match {url}'

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(self.driver.window_handles[1])