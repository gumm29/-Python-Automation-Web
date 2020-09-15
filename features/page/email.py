from page_objects import PageObject, PageElement

class Email(PageObject):
  h1_email = PageElement(css = 'div[id="form"] h1')