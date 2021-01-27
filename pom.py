from selenium.webdriver.common.by import By
from base_element import BaseElement
class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    @property
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1])

    def close_browser(self):
        self.driver.close()
        return None


# Test smoke
from selenium import webdriver

# setup
browser = webdriver.Chrome()
test_value = 'it worked!!'

# Test
trn_page = TrainingGroundPage(driver=browser)
trn_page.go()
assert trn_page.button1.get_text == 'Button1'
trn_page.close_browser()





