from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")
print("Title:", driver.title)
print("Current URL:", driver.current_url)

driver.quit()
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")
print("Page 1:", driver.current_url)

driver.get("https://www.saucedemo.com/inventory.html")  # note: this will actually redirect you back to login, since you're not logged in - that's expected!
print("Page 2:", driver.current_url)

driver.back()
print("After back():", driver.current_url)

driver.forward()
print("After forward():", driver.current_url)

driver.refresh()
print("After refresh():", driver.current_url)

time.sleep(2)  # just so you can see the last state before it closes
driver.quit()
class BrowserSession:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        print("Opened:", self.driver.current_url)

    def close(self):
        self.driver.quit()

session = BrowserSession("https://www.saucedemo.com")
session.open()
session.close()

class BrowserSession:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        print("Opened:", self.driver.current_url)

    def get_title(self):
        return self.driver.title

    def close(self):
        self.driver.quit()

session = BrowserSession("https://www.saucedemo.com")
session.open()
print("Title:", session.get_title())
session.close()