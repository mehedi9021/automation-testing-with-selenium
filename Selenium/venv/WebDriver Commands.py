from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

driver.__exit__()