from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.facebook.com/")

email_check = driver.find_element_by_name("email")

print(email_check.is_displayed())
print(email_check.is_enabled())

pass_check = driver.find_element_by_name("pass")

print(pass_check.is_displayed())
print(pass_check.is_enabled())

email_check.send_keys("mm*****gmail.com")
pass_check.send_keys("*****")

driver.find_element_by_name("login").click()

time.sleep(5)
driver.__exit__()
