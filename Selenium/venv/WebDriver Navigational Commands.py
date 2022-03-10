from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.facebook.com/")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

time.sleep(5)

driver.__exit__()