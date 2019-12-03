from selenium.webdriver import Chrome
from library.ConfigReader import *


def before_all(context):
    print("Before all")
    context.driver = Chrome(executable_path=getConstants("Details","DriverPath"))
    context.driver.maximize_window()


def after_all(context):
    print("After all")
    context.driver.quit()


def before_feature(context, feature):
    pass
    # print("before feature")
    # context.driver = Chrome(executable_path="./drivers/chromedriver.exe")


def after_feature(context, feature):
    pass
    # print("after feature")
    # context.driver.quit()


def before_scenario(context, scenario):
    pass
    # print("before scenario")
    # context.driver = Chrome(executable_path="./drivers/chromedriver.exe")
    # context.driver.maximize_window()


def after_scenario(context, scenario):
    pass
    # print("after scenario")
    # context.driver.quit()


def before_step(context, step):
    print("before step")


def after_step(context, step):
    pass
    # print("after step")


def before_tag(context, tag):
    pass
    # print("before tag")
    # context.driver = Chrome(executable_path="./drivers/chromedriver.exe")
    # context.driver.maximize_window()


def after_tag(context, tag):
    pass
    # print("after tag")
    # context.driver.quit()








