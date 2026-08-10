from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
login_credentials = driver.find_element(By.CLASS_NAME, "login_credentials_wrap")
print("Found login credentials box:", login_credentials)


print("Found username field:", username_field)
print("Found password field:", password_field)
print("Found login button:", login_button)
print("Found login credentials box:", login_credentials)

driver.quit()