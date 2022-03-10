from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element_by_class_name("uitk-tab-anchor uitk-tab-anchor-selected").click()
