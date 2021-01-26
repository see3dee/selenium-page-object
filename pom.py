


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver=driver
        self.url = ''
        pass

    def type_into_input(self, text):
        input_field = self.driver.find_element_ by_id('lpt1')
        input_field.clear()
        input_field.send_keys(text)
        return None

    def get_input_text(self):
        input_field = self.driver.find_element_by_id('lpt1')
        elem_text = input_field.get_attribute('value')
        return elem_text

    def click_button(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None



