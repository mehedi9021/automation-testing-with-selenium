from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.facebook.com/")


#wait to completely load the webpage-> implicit wait(is applicable for all elements)

driver.implicitly_wait(50)

driver.find_element_by_name("email").send_keys("mm*******gmail.com")
driver.find_element_by_name("pass").send_keys("*****")
driver.find_element_by_name("login").click()

time.sleep(5)
driver.__exit__()