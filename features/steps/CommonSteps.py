from behave import *
from library.ConfigReader import *


@given(u'I am at login page of OrangeHrm')
def launchApplication(context):
    context.driver.get(getConstants("Details","Application_Url"))


@when(u'I do page refresh')
def reloadePage(context):
    context.driver.refresh()