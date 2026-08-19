from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait specifically for the dropdown to be clickable, then use the returned element directly
dropdown_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "select.product_sort_container"))
)
sort_dropdown = Select(dropdown_element)
sort_dropdown.select_by_value("hilo")

first_price_hilo = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
print("First item's price after sorting high to low:", first_price_hilo)

driver.quit()