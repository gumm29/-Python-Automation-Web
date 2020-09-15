from environment import *
from page.home import *
from page.email import *
from support.commons import *

@given('access the site')
def step_impl(context):
  site(context)


@when('click in email button')
def step_impl(context):
  page = Home(context.browser)
  page.btn_email.click()


@then('check email page')
def step_impl(context):
  page = Email(context.browser)
  print(page.h1_email.text)
  assert page.h1_email.text == 'Login'