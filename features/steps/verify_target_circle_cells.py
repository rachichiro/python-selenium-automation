from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Circle Website')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)

@then('Verify there are at least 10 Benefit Cells')
def verify_cells(context):
    cells = context.driver.find_elements(By.XPATH,"//div[@class='cell-item-content']")
    print(cells)

    assert len(cells) >= 10, f'expected 10 or more links but found {len(cells)}'

