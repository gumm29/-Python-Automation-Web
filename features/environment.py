from selenium import webdriver
import yaml

MASSA = yaml.safe_load(open('support/data/data.yml'))
CONFIG = yaml.safe_load(open('support/config/config.yml'))

def before_all(context):
  context.browser = webdriver.Firefox()
  context.browser.implicitly_wait(60)

def after_all(context):
  context.browser.quit()