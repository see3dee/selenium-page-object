from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "b1"))
    )
finally:
    browser.quit()



