from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Sort: Price low to high
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.product_sort_container"))
sort_dropdown.select_by_visible_text("Price (low to high)")
time.sleep(1)

first_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
print("First item's price after sorting low to high:", first_price)

# Re-find fresh before reading .options, since the sort action re-rendered the page
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.product_sort_container"))
print("All available sort options:")
for option in sort_dropdown.options:
    print("-", option.text, "| value:", option.get_attribute("value"))

# Sort: Price high to low - re-find again since we're selecting a NEW option
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.product_sort_container"))
sort_dropdown.select_by_value("hilo")
time.sleep(1)

first_price_hilo = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
print("First item's price after sorting high to low:", first_price_hilo)

# Re-find fresh again before the final loop
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.product_sort_container"))
target_value = None
for option in sort_dropdown.options:
    if option.text == "Name (Z to A)":
        target_value = option.get_attribute("value")

print("The value for 'Name (Z to A)' is:", target_value)

driver.quit()