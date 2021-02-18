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

# Test (force fail)
trn_page = TrainingGroundPage(driver=browser)
trn_page.go()
test_value = 'Button2'
assert trn_page.button1.get_text == test_value, f"test_value {test_value} was not asserted, " \
                                                f"actual value was {trn_page.button1.get_text}"
trn_page.close_browser()





