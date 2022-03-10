from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.facebook.com/")

print(driver.title)

print(driver.current_url)

print(driver.page_source)

driver.close()