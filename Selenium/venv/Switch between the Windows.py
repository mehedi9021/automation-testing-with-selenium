from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)  #CDwindow-AAD7E72D569DEFFB09C1900E7F76E6A6 parent window handle value

print(driver.window_handles)         #return all window handle values

handles = driver.window_handles

#return all the window title
for handle in handles:
    driver.switch_to.window(handle) #switch to another window
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()    #close a specific window