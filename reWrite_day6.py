from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

print("Username field:", username_field)
print("Password field:", password_field)
print("Login button:", login_button)

driver.quit()