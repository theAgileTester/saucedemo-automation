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

products_title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
)

actual_title = products_title.text
expected_title = "Products"
assert actual_title == expected_title, f"Expected page title '{expected_title}' but got '{actual_title
}'"
print("PASSED: Login successful, correct page title shown")

# driver.get("https://www.saucedemo.com")
# driver.find_element(By.ID, "user-name").send_keys("wrong_user")
# driver.find_element(By.ID, "password").send_keys("wrong_pass")
# driver.find_element(By.ID, "login-button").click()

# error_message = WebDriverWait(driver, 10).until(
   #  EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))


# assert "do not match" in error_message.text, f"Expected a mismatch error, but got: '{error_message.text}'"
# print("PASSED: Invalid login correctly shows an error") 

# Sort: Price low to high
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.product_sort_container"))
sort_dropdown.select_by_visible_text("Price (low to high)")

first_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
print("First item's price after sorting low to high:", first_price)

assert first_price == "$7.99", f"Expected first item's price to be '$7.99', but got '{first_price}'"
print("PASSED: Products correctly sorted by price, low to high")


driver.quit()

