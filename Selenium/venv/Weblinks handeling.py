from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

#find out total links in webpage
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
#or
links = driver.find_elements(By.CLASS_NAME, "link")
print(len(links))

for link in links:
    print(link.text)

#open links
#driver.find_element(By.LINK_TEXT, "Software Testing Tutorials").click()
#or
driver.find_element(By.PARTIAL_LINK_TEXT, "Software Testing").click()