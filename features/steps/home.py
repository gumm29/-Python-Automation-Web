from page.home import Home
from page.email import Email
from support.commons import site

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
  assert page.h1_email.text == 'Login'