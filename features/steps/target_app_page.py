from time import sleep

from behave import  given,when,then
from selenium.webdriver.common.devtools.v85.page import add_script_to_evaluate_on_new_document


@given ('Open Target App Page')
def open_target_app(context):
 context.app.target_app_page.open_target_app()

 @then ('Store Original Window')
 def store_original_window(context):
     context.original_window = context.app.target_app_page.get_current_window_handle()

 @when ('Click Privacy Policy Link')
 def click_privacy_policy(context):
     context.app.target_app_page.click_privacy_policy()

 @then ('Switch to New Window')
 def switch_to_new_window(context):
     sleep(3)
     print('All Windows',context.driver.window_handles)
     context.driver.switch_to.window(context.driver.window_handles[1])

 #@then ('Verify Privacy Policy Window Opened')

 #@then ('Close Current Window')

 #@then ('Return to Original Window')

