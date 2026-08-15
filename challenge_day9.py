from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-features=PasswordLeakDetection")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")

user_name_field = driver.find_element(By.ID, "user-name")
user_name_field.clear()
user_name_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

time.sleep(3)  # longer wait, to rule out timing entirely

# DIAGNOSTICS - tell us exactly what's happening
print("Current URL:", driver.current_url)
badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
print("Number of badges found:", len(badges))

if len(badges) > 0:
    print("Cart badge text:", badges[0].text)
else:
    print("Badge not found - button text is now:", add_to_cart_button.text)

driver.quit()