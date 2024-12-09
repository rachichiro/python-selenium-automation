from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get('https://www.amazon.com/')
sleep(10)

driver.find_element(By.XPATH,  "//*[@id='nav-link-accountList']").click()
sleep(2)

##find amazon logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']")

##find email field
driver.find_element(By.ID,"ap_email")

##find continue button
driver.find_element(By.ID,"continue")

##find privacy link
driver.find_element(By.XPATH,"//a[contains(@href,'signin_notification_privacy')]")

##find conditions of use link
driver.find_element(By.XPATH,"//a[contains(@href,'signin_notification_condition')]")

##find help link & click for drop down of other needed locators
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']").click()
sleep(4)

##forgot password link
driver.find_element(By.ID,"auth-fpp-link-bottom")

##other issues with sign in link
driver.find_element(By.ID,"ap-other-signin-issues-link")

##create your amazon account button
driver.find_element(By.ID,"createAccountSubmit")