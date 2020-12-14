from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/iframe-training')

#  define this iframe it is the only iframe on the page
iframe = browser.find_element_by_css_selector("iframe")

# switch to that iframe element
browser.switch_to.frame(iframe)
iframe_para_xpath = "//div[@id = 'block-ec928cee802cf918d26c']/div/p"
iframe_para_text = browser.find_element_by_xpath(iframe_para_xpath).text
# switch Back to Base page:
browser.switch_to.default_content()

# grab/assert header title on base page
HeaderTitleText = browser.find_element_by_css_selector('#lower-logo > h1 > a').text
assert HeaderTitleText == "TECHSTEP ACADEMY"

browser.quit()