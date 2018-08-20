# Automating Instagram Likes

# Import Libraries 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Launch Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(15)
# driver.maximize_window()

# Navigate to URL
driver.get('https://instagram.com')

# Redirect to Login from Signup
redirect_login_element = driver.find_element_by_css_selector('.izU2O > a:nth-child(1)')
redirect_login_element.click()

# Send username and password
driver.find_element_by_xpath('//*[@name="username"]').send_keys('username')
driver.find_element_by_xpath('//*[@name="password"]').send_keys('password')

# Click login Link
login_element = driver.find_element_by_css_selector("._5f5mN")
login_element.click()

# Notifications Screen
# This may not be required if an account has notifications "on" 
turnOffNotifications = driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
turnOffNotifications.click()

# Feed URLs from Text File
with open("autoRounds.txt") as file:
    urls = file.read()

for url in urls:                                                              
    driver.get(url)

# Exit Browser when finished
browser.close()
