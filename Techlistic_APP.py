import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("sidraya")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("shegunshi")

driver.find_element(By.XPATH,"//input[@id='sex-0']").click()
driver.find_element(By.XPATH,"//input[@id='exp-0']").click()

driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("12/03/2022")

driver.find_element(By.XPATH,"//input[@id='profession-0']").click()
driver.find_element(By.XPATH,"//input[@id='tool-1']").click()



# drop down visible by text method

# Drp_element=driver.find_element(By.XPATH,"//select[@id='continents']")
# Drp_op = Select(Drp_element)
# Drp_op.select_by_visible_text('Europe')
# time.sleep(2)

# drop down visible by index method

Drp_element=driver.find_element(By.XPATH,"//select[@id='continents']")
Drp_op = Select(Drp_element)
Drp_op.select_by_index("5")

#### dropdown method

Drp_elements=driver.find_element(By.XPATH,"//*[@id='selenium_commands']")
Drp_cmd=driver.find_element(By.XPATH,"//option[contains(text(),'Wait Commands')]")
Drp_cmd = Select(Drp_elements)
time.sleep(2)

# script for the upload imgae(file)
file_path=os.path.join(os.getcwd(),"C:/Users/sidsh/OneDrive/Pictures/download.jpeg")
file_input=driver.find_element(By.XPATH,"//input[@id='photo']")
file_input.send_keys(file_path)

# download file
download_file=driver.find_element(By.XPATH,"//a[contains(text(),'Click here to Download File')]")
download_file.click()
time.sleep(2)



