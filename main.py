from selenium import webdriver
import css_xpath_trial

# Trial of the stones

driver = webdriver.Chrome()
driver.get('https://techstepacademy.com/trial-of-the-stones')

inpt1 = driver.find_element_by_css_selector(css_xpath_trial.inpt1_css)
inpt1.send_keys('rock')

butn1 = driver.find_element_by_css_selector(css_xpath_trial.ans_butn1_css)
butn1.click()

passwd = driver.find_element_by_css_selector(css_xpath_trial.passwd_css).text



inpt2 = driver.find_element_by_css_selector(css_xpath_trial.inpt2_css)
inpt2.send_keys(passwd)

butn2 = driver.find_element_by_css_selector(css_xpath_trial.ans_butn2_css)
butn2.click()
msg2 = driver.find_element_by_css_selector(css_xpath_trial.msg2_css).text
assert msg2 == 'Success!', f"'Success!' was expected but '{msg2}' was displayed."

rich_merch = driver.find_element_by_xpath("//p[text() = '3000']/../span").text

inpt3 = driver.find_element_by_css_selector(css_xpath_trial.inpt3_css)
inpt3.send_keys(rich_merch)
butn3 = driver.find_element_by_css_selector(css_xpath_trial.ans_butn3_css)
butn3.click()
msg3 = driver.find_element_by_css_selector(css_xpath_trial.msg3_css).text
assert msg3 == 'Success!', f"'Success!' was expected but '{msg3}' was displayed."

check_butn = driver.find_element_by_css_selector(css_xpath_trial.final_check_butn_css)
check_butn.click()
trial_comp_msg = driver.find_element_by_css_selector('#trialCompleteBanner > h4').text
assert trial_comp_msg == 'Trial Complete', f"'Trail Complete' was expected but '{trial_comp_msg}' was displayed."
driver.quit()









