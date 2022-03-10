from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:\Pass-Port Photo.jpg")

time.sleep(5)

