from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASE_URL = "https://www.saucedemo.com"


def test_valid_login_shows_products_page(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )
    assert products_title.text == "Products", f"Expected 'Products' but got '{products_title.text}'"


@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "wrong_pass", "do not match"),
    ("standard_user", "wrong_pass", "do not match"),
    ("", "", "Username is required"),
])
def test_multiple_invalid_logins(driver, username, password, expected_error):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert expected_error in error_message.text, f"Expected '{expected_error}' but got: '{error_message.text}'"