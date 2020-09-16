from environment import CONFIG

def site(context):
  context.browser.get(CONFIG['url'])