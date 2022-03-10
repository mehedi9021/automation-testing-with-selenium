from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("file:///C:/Users/User/PycharmProjects/Selenium/venv/table.html")

rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr")
col = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")

print(len(rows))
print(len(col))

print("Company"+"    "+"Contact"+"    "+"Country")

for r in range (2, 6):
    for c in range (1, 4):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='    ')
    print()