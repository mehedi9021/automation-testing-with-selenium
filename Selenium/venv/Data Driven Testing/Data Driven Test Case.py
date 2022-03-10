import XLutills
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.coursera.org/login")
driver.maximize_window()

path = "C:\write.xlsx"

#rows count
rows = XLutills.getRowCount(path, 'Sheet1')
columns = XLutills.getColumnCount(path, 'Sheet1')

print(rows)
print(columns)

for r in range (2, rows+1):
    username = XLutills.readData(path, 'Sheet1', r, 1)
    password = XLutills.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//*[@id='rendered-content']/div/div/div/div/div/section/section/div[1]/form/button").click()

    if driver.title == "Daffodil International University | Coursera":
        print("test is passed!!")
        XLutills.writeData(path, 'Sheet1', r, 3, "test passed")
    else:
        print("test failed!!")
        XLutills.writeData(path, 'Sheet1', r, 3, "test failed")

    driver.find_element_by_link_text("Log Out").click()