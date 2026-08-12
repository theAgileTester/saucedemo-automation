
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

time.sleep(2)  # give the inventory page time to fully load

# find it fresh, right before clicking - not before login
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

time.sleep(5)  # keep browser open so you can see the result
driver.quit()