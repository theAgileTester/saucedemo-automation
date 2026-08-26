import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_valid_login_shows_products_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    actual_title = products_page.get_title_text()
    assert actual_title == "Products", f"Expected 'Products' but got '{actual_title}'"

    actual_url = products_page.get_current_url()
    assert "inventory.html" in actual_url, f"Expected URL to contain 'inventory.html' but got '{actual_url}'"


@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "wrong_pass", "do not match"),
    ("standard_user", "wrong_pass", "do not match"),
    ("", "", "Username is required"),
])
def test_multiple_invalid_logins(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    actual_error = login_page.get_error_message()
    assert expected_error in actual_error, f"Expected '{expected_error}' but got: '{actual_error}'"
