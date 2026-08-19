from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# Add to Cart button test
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

cart_badge = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
)

assert cart_badge.text == "1", f"Expected shopping cart badge to show '1', but it shows '{cart_badge.text}'"
print("PASSED: Shopping cart badge correctly shows '1' after adding an item to the cart")

