from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

print("Username field:", username_field)
print("Password field:", password_field)
print("Login button:", login_button)

username_field.send_keys("wrong_user")
password_field.send_keys("wrong_pass")
login_button.click()
time.sleep(1)

error_message = driver.find_element(By.XPATH, "//h3[contains(text(), 'sadface')]")
print("Error message found via text match:", error_message.text)

# Find the password field, then go UP to its parent container
password_parent = driver.find_element(By.XPATH, "//input[@id='password']/..")
print("Password field's parent element:", password_parent)

driver.quit()