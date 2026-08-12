from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

print("Username field:", username_field)
print("Password field:", password_field)
print("Login button:", login_button)
logo = driver.find_element(By.CSS_SELECTOR, "div.login_logo")
print("Logo:", logo)

username_field_by_attr = driver.find_element(By.CSS_SELECTOR, "[data-test='username']")
print("Username field (by data-test):", username_field_by_attr)
username_field.send_keys("wrong_user")
password_field.send_keys("wrong_pass")
login_button.click()

import time
time.sleep(1)  # give the page a moment to show the error

error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
print("Error message:", error_message.text)

driver.quit()