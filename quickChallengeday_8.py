
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")   

print("Username field:", username_field)
print("Password field:", password_field)
print("Login button:", login_button)
print("Add to cart button:", add_to_cart_button)
logo = driver.find_element(By.XPATH, "//div[@class='login_logo']")
print("Logo:", logo)

username_field_by_attr = driver.find_element(By.XPATH, "//input[@data-test='username']")
print("Username field (by data-test):", username_field_by_attr)
username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_credentials = driver.find_element(By.XPATH, "//div[@class='login_credentials_wrap']")
print("Found login credentials box:", login_credentials)

import time
time.sleep(1)  # give the page a moment to show the error

driver.quit()