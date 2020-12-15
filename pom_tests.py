from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traininggroundpage as tgp

# test setup
browser = webdriver.Chrome()
test_text = 'It Worked!!!'

# Test
trng_page = tgp.TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_text)
assert trng_page.get_input_text() == test_text
trng_page.close_browser()







