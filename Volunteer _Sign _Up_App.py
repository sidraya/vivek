import time
import os.path

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # when use dropdown that time use selelect Method

driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-1']").send_keys("raju")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-2']").send_keys("Bhirdkar")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-3']").send_keys("8888727350")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-4']").send_keys("India")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-5']").send_keys("Pune")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-6']").send_keys("raju@gmail.com")

driver.find_element(By.XPATH,"//label[contains(text(),'Male')]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//label[contains(text(),'Sunday')]").click()
time.sleep(2)

# DRop down method  by using text by visible method    ###############
drp_element=driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-9']")
drp_opt=Select(drp_element)
drp_opt.select_by_visible_text("Morning")
time.sleep(5)


########  use dropdoen method buy using index method    ############

drp_element=driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-9']")
drp_opt=Select(drp_element)
drp_opt.select_by_index("2")
time.sleep(5)

# script for the upload imgae(file)
file_path=os.path.join(os.getcwd(),"C:/Users/sidsh/OneDrive/Pictures/download.jpeg")
file_input=driver.find_element(By.XPATH,"//input[@id='RESULT_FileUpload-10']")
file_input.send_keys(file_path)
time.sleep(2)

# click submit button


#
#
#
# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_form_submission(setup):
#     driver = setup
#     driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-1']").send_keys("raju")
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").send_keys("Bhirdkar")
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-3']").send_keys("8888727350")
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-4']").send_keys("India")
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']").send_keys("Pune")
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-6']").send_keys("raju@gmail.com")
#
#     driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
#     time.sleep(2)
#
#     driver.find_element(By.XPATH, "//label[contains(text(),'Sunday')]").click()
#     time.sleep(2)
#
#     # Correctly locate the <select> element and use it
#     drp_element = driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-9']")
#     drp_opt = Select(drp_element)
#     drp_opt.select_by_visible_text("Morning")
#
#     time.sleep(5)
#
#     # Optional: Add assertions here to validate form submission or other actions
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-1']").get_attribute("value") == "raju"
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").get_attribute("value") == "Bhirdkar"
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-3']").get_attribute("value") == "8888727350"
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-4']").get_attribute("value") == "India"
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']").get_attribute("value") == "Pune"
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-6']").get_attribute("value") == "raju@gmail.com"
#
#     # Verify the selected option in the dropdown
#     selected_option = drp_opt.first_selected_option
#     assert selected_option.text == "Morning"
#
# if __name__ == "__main__":
#     pytest.main(["-v", "test_form_submission.py"])


# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# @pytest.fixture
# def setup():
#     # Setup WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_form_submission(setup):
#     driver = setup
#
#     # Step 1: Open the target URL
#     driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
#     # Step 2: Enter 'First Name'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-1']").send_keys("raju")
#
#     # Step 3: Enter 'Last Name'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").send_keys("Bhirdkar")
#
#     # Step 4: Enter 'Phone'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-3']").send_keys("8888727350")
#
#     # Step 5: Enter 'Country'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-4']").send_keys("India")
#
#     # Step 6: Enter 'City'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']").send_keys("Pune")
#
#     # Step 7: Enter 'Email'
#     driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-6']").send_keys("raju@gmail.com")
#
#     # Step 8: Select 'Gender' as 'Male'
#     driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
#     time.sleep(2)
#
#     # Step 9: Select 'Day' as 'Sunday'
#     driver.find_element(By.XPATH, "//label[contains(text(),'Sunday')]").click()
#     time.sleep(2)
#
#     # Step 10: Select 'Best Time to Contact' as 'Morning' from dropdown
#     drp_element = driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-9']")
#     drp_opt = Select(drp_element)
#     drp_opt.select_by_visible_text("Morning")
#     time.sleep(5)
#
#     # Step 11: Assertion - Verify 'First Name' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-1']").get_attribute("value") == "raju"
#
#     # Step 12: Assertion - Verify 'Last Name' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").get_attribute("value") == "Bhirdkar"
#
#     # Step 13: Assertion - Verify 'Phone' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-3']").get_attribute("value") == "8888727350"
#
#     # Step 14: Assertion - Verify 'Country' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-4']").get_attribute("value") == "India"
#
#     # Step 15: Assertion - Verify 'City' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']").get_attribute("value") == "Pune"
#
#     # Step 16: Assertion - Verify 'Email' field value
#     assert driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-6']").get_attribute("value") == "raju@gmail.com"
#
#     # Step 17: Assertion - Verify selected option in 'Best Time to Contact' dropdown
#     selected_option = drp_opt.first_selected_option
#     assert selected_option.text == "Morning"
#
# if __name__ == "__main__":
#     pytest.main(["-v", "test_form_submission.py"])
