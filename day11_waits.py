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

# Instead of time.sleep(2), wait SPECIFICALLY for the products page to be ready
products_title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
)
print("Page heading text:", products_title.text)
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_to_cart_button.click()

cart_badge = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
)
print("Cart badge text:", cart_badge.text)

driver.quit()