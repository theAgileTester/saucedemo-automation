from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_item_to_cart_updates_badge(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_item_to_cart("backpack")

    badge_count = products_page.get_cart_badge_count()
    assert badge_count == "1", f"Expected cart badge to show '1' but got '{badge_count}'"


def test_sort_by_price_low_to_high(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.sort_by("lohi")

    first_price = products_page.get_first_item_price()
    assert first_price == "$7.99", f"Expected '$7.99' but got '{first_price}'"
