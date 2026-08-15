from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

# Login

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Find sorting dropdown

sort_dropdown_element = driver.find_element(
    By.CSS_SELECTOR,
    "select.product_sort_container"
)

sort_dropdown = Select(sort_dropdown_element)

# Sort: Price low to high

sort_dropdown.select_by_visible_text("Price (low to high)")

time.sleep(1)

# Verify first product price

first_price = driver.find_element(
    By.CSS_SELECTOR,
    ".inventory_item_price"
).text

print("First item's price after sorting low to high:", first_price)

# Print all available sort options

print("All available sort options:")

sort_dropdown_element = driver.find_element(
    By.CSS_SELECTOR,
    "select.product_sort_container"
)

sort_dropdown = Select(sort_dropdown_element)

for option in sort_dropdown.options:
    print("-", option.text, "| value:", option.get_attribute("value"))
# Sort: Price high to low

sort_dropdown.select_by_value("hilo")

time.sleep(1)

# Verify first product price

first_price_hilo = driver.find_element(
    By.CSS_SELECTOR,
    ".inventory_item_price"
).text

print("First item's price after sorting high to low:", first_price_hilo)

driver.quit()