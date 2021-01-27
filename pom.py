class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('ipt1')
        inpt.clear()
        inpt.send_keys(text)

    def get_input_text(self):
        inpt = self.driver.find_element_by_id('ipt1')
        elem_test = inpt.get_attribute('value')
        return elem_test

    def click_button_1(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None
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
trn_page.type_into_input(test_value)
text_from_input = trn_page.get_input_text()
assert text_from_input == 'it worked!!', f"The test value was not asserted, actual value was '{test_value}'"
trn_page.close_browser()





