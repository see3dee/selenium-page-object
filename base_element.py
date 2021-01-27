from selenium.webdriver.common.by import By

'''
Selenium web element is defined by the 
BY (type of selector) and the Locator (string representation 
of the type's path to the element)
'''

class BaseElement(object):
    def __init__(self, driver, locator, by):
        self.driver = driver
        self.locator = locator
        self.by = by
        self.web_element = None

    def find(self):
        self.driver.find_element(by=self.by, value=self.locator)




