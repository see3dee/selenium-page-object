from selenium import webdriver

# Creating Windows:
browser1 = webdriver.Firefox()
browser2 = webdriver.Chrome()

browser1.get('https://www.google.com')
browser2.get('https://www.amazon.com')

browser1.get('https://www.amazon.com')
browser2.get('https://www.google.com')

browser1.quit()
browser2.quit()

#  Creating tabs:
browser3 = webdriver.Chrome()
browser3.get('http://techstepacademy.com/training-ground')

browser3.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser3.execute_script('window.open("https://www.google.com","_blank");')
browser3.execute_script('window.open("https://www.ebay.com","_blank");')
browser3.execute_script('window.open("https://www.amazon.com","_blank");')

browser3.quit()