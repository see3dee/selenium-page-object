from selenium import webdriver


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('lpt1')
        inpt.clear()
        inpt.send_keys(text)

    def get_input_text(self):
        inpt = self.driver.find_element_by_id('lpt1')
        elem_test = inpt.get_attrinute('value')
        return elem_test

    def click_button_1(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None







