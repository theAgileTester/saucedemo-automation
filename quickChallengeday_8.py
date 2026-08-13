from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")   # Step 1: we are on the LOGIN page now

# Step 2: these three elements DO exist on the login page - safe to find here
username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Step 3: type credentials and submit - this is what moves us to the NEXT page
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

time.sleep(2)  # give the inventory page time to load

# Step 4: ONLY NOW does this button exist, because we're on inventory.html
add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@id, 'backpack')]")
add_to_cart_button.click()

# Step 5: this can happen anytime, since the logo exists on the LOGIN page, not inventory
# (so actually this needs to happen back on the login page - see note below)

time.sleep(3)
driver.quit()
