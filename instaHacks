# Automating Instagram Likes

# Import Libraries 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Launch Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to URL
driver.get("https://instagram.com")

# Redirect to Login from Signup
redirect_login_element = driver.find_element_by_css_selector('.izU2O > a:nth-child(1)')
redirect_login_element.click()

# Send username and password
# Not working, CSS and Xpath dynamic....
driver.find_element_by_xpath("//*[@id=\"f3ef0e7f67ebb64\"]").send_keys("username")
driver.find_element_by_xpath("//*[@id=\"f2c74ebcad4cf8e\"]").send_keys("password")

# Click login Link
login_element = driver.find_element_by_css_selector("._5f5mN")
login_element.click()

# Like a photo
# Only Links first photo, setup loop
like_element = driver.find_element_by_css_selector("article._8Rm4L:nth-child(1) > div:nth-child(3) > section:nth-child(1) > span:nth-child(1) > button:nth-child(1)")
like_element.click()

# Exit Browser when finished
browser.close()


