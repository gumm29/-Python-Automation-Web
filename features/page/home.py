from page_objects import PageObject, PageElement

class Home(PageObject):
  btn_email = PageElement(class_name = 'HU_blackBar_listServices__service__email__label')