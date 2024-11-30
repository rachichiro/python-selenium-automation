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


driver.get('https://www.target.com/')
driver.find_element(By.ID,'account-sign-in').click()
sleep(2)
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

sleep(2)

driver.find_element(By.XPATH,"//*[text()='Sign into your Target account']")

sleep(5)

expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text

assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')
sleep(2)

driver.find_element(By.ID,'login')
