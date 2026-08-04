from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
print("Page title is:", driver.title)
driver.quit()