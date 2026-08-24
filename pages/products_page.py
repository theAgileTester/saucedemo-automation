from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    TITLE = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE)
        )
        return title_element.text

    def get_current_url(self):
        return self.driver.current_url
