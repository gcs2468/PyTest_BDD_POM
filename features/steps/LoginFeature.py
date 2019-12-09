import allure
from behave import *
from time import sleep
from library.ConfigReader import *


@then('Verify the title')
def verifyTitle(context):
    assert context.driver.title == "OrangeHRM"


@then('Verify the title two')
def verifyTitle(context):
    assert context.driver.title == "OrangeHRM"
    # context.driver.save_screenshot('screenshot.png')


@when('I enter "Admin" in username field')
def enterUserName(context):
    context.driver.find_element_by_xpath(getLocators("LoginPage","txtUsername")).send_keys("Admin")
    # sleep(5)


@when('I enter "admin123" in password field')
def step_impl(context):
    context.driver.find_element_by_xpath(getLocators("LoginPage","txtPassword")).send_keys("admin123")
    # sleep(5)


@when('I click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath(getLocators("LoginPage","btnLogin")).click()
    sleep(5)


@then('I should see Welcome Admin text')
def step_impl(context):
    assert context.driver.find_element_by_xpath(getLocators("LoginPage","welcome")).text == "Welcome Admin"


@then('I should see admin image')
def step_impl(context):
    pass

@when('I enter {username} in userid field')
def step_impl(context, username):
    context.driver.find_element_by_xpath(getLocators("LoginPage","txtUsername")).send_keys(username)
    # sleep(5)


@when('I enter {password} in password field')
def step_impl(context, password):
    context.driver.find_element_by_xpath(getLocators("LoginPage","txtPassword")).send_keys(password)
    # sleep(5)

@then('I click on logout button')
def logoutAppln(context):
    context.driver.find_element_by_xpath(getLocators("LoginPage","welcome")).click()
    sleep(3)
    context.driver.find_element_by_xpath(getLocators("LoginPage","Logout")).click()
    sleep(3)