from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")

username_field.send_keys("standard_user")
print("After first send_keys:", username_field.get_attribute("value"))

username_field.send_keys("_extra_text")
print("After second send_keys (no clear):", username_field.get_attribute("value"))

username_field.clear()
print("After clear():", username_field.get_attribute("value"))

username_field.send_keys("standard_user")
print("After clear + send_keys:", username_field.get_attribute("value"))

password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

password_field.clear()
password_field.send_keys("secret_sauce")
login_button.click()

time.sleep(2)

products_title = driver.find_element(By.CSS_SELECTOR, ".title")
print("Page heading text:", products_title.text)

driver.quit()