from selenium import webdriver

# Creating Windows:
# browser1 = webdriver.Firefox()
# browser2 = webdriver.Chrome()
#
# browser1.get('https://www.google.com')
# browser2.get('https://www.amazon.com')
#
# browser1.get('https://www.amazon.com')
# browser2.get('https://www.google.com')
#
# browser1.quit()
# browser2.quit()

#  Creating tabs:
browser3 = webdriver.Chrome()
browser3.get('https://techstepacademy.com/training-ground')

browser3.execute_script('window.open("https://www.google.com","_blank");')
# browser3.execute_script('window.open("https://www.ebay.com","_blank");')
# browser3.execute_script('window.open("https://www.amazon.com","_blank");')


handles = browser3.window_handles
for tab in handles:
    print(tab)

assert len(handles) == 2, f'Expected number of tabs was 2 actual was {len(handles)}'

browser3.switch_to.window(handles[0])
assert browser3.current_url == 'https://techstepacademy.com/training-ground'

browser3.quit()