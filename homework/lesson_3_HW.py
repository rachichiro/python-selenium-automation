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
sleep(5)

driver.find_element(By.ID,  "nav-link-accountList").click()
sleep(2)

driver.find_element(By.ID,"createAccountSubmit").click()

##find amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

##verify create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

##verify name
driver.find_element(By.ID,"ap_customer_name")

##verify email
driver.find_element(By.ID,"ap_email")

##verify password
driver.find_element(By.ID,"ap_password")

##verify re-enter password
driver.find_element(By.ID,"ap_password_check")

##verify create account link
driver.find_element(By.ID,"continue")

##verify conditions of use
driver.find_element(By.XPATH,"//a[contains(@href,'ap_register_notification_condition_of_use')]")

##verify privacy notice
driver.find_element(By.XPATH,"//a[contains(@href,'ap_register_notification_privacy')]")

##verify sign in button
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")