from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ProductsPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    FIRST_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE)
        )
        return title_element.text

    def get_current_url(self):
        return self.driver.current_url

    def add_item_to_cart(self, item_id):
        locator = (By.ID, f"add-to-cart-sauce-labs-{item_id}")
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def get_cart_badge_count(self):
        badge = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def sort_by(self, value):
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown_element).select_by_value(value)

    def get_first_item_price(self):
        price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_ITEM_PRICE)
        )
        return price_element.text
