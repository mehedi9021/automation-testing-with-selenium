from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

#count input boxes

inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

#put values to the boxes

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Md. Mehedi")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Hasan")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("0162344****")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Bangladesh")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Dhaka")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("mm*********gmail.com")

#input values for radio button

#first need to find out wheather the radiobutton is selected or not

status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected() #for male
print(status)
status = driver.find_element(By.ID, "RESULT_RadioButton-7_1").is_selected() #for female
print(status)

#select radio button

driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()

#select check box

driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[4]/td/label")


# select dropdown option

element = driver.find_element_by_id("RESULT_RadioButton-9")
dropdown = Select(element)
#approach 1
dropdown.select_by_index(2)
#approach 2
#dropdown.select_by_value("Radio-2")
#approach 3
#dropdown.select_by_visible_text("Evening")

#count the total options in dropdown

print(len(dropdown.options))

#print all the options in the doropdown

all_options = dropdown.options
for option in all_options:
    print(option.text)




time.sleep(5)

driver.__exit__()