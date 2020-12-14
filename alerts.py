from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import css_xpath_trial

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

print('getting started')
alert_popup = Alert(browser)

butn1_css = "button[name = 'butn1']"
butn1 = browser.find_element_by_css_selector(butn1_css)
butn1.click()

print(f' The alert says: {alert_popup.text}')
alert_popup.accept()

browser.quit()