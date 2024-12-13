import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(4)
chrome_driver.find_element(By.NAME,"name").send_keys("ashuuser")
chrome_driver.find_element(By.NAME,"email").send_keys("sapvin24@gmail.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("selvi")
chrome_driver.find_element(By.ID,"exampleCheck1").click
# selectgen = chrome_driver.find_element(By.XPATH, "//*[text()='Female']")
# selectgen.click()
seloption = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))

seloption.select_by_index(1)
time.sleep(5)

#chrome_driver.find_element(By.CSS_SELECTOR,"inlineRadio1").click

chrome_driver.find_element(By.XPATH, '//*[@id="dob"]').send_keys('01/15/1990')

# Submit the form
submit_button = chrome_driver.find_element(By.XPATH, '//*[@id="submit"]')
submit_button.click()

# Wait for the success message to be visible and capture it
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="success-message"]'))
).text

print("Success message:", success_message)

# date_picker = By.element_to_be_clickable((By.ID, "datepicker_id"))   
# date_picker.click()   
# date = By.element_to_be_clickable((By.XPATH, "//td[text()='15']"))   
# date.click()  # Click on the da

# # Select the day
# day = chrome_driver.find_element(By.CSS_SELECTOR, "a.ui-state-default[data-date='15']")
# day.click()

# # Submit the form
# submit_button = chrome_driver.find_element(By.CSS_SELECTOR, '#submit')
# submit_button.click()

# # Wait for the success message to be visible and capture it
# success_message = By.visibility_of_element_located((By.CSS_SELECTOR, '#success-message')).text

time.sleep(30)
print("page title", chrome_driver.title)
print("page title", chrome_driver.current_url)
chrome_driver.save_screenshot("pag1.png")
print("page1 screenshot saved")
chrome_driver.quit()