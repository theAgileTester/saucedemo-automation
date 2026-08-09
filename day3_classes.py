class LoginPage:
    def __init__(self, url):
        self.url = url

page = LoginPage("https://www.saucedemo.com")
print(page.url)
class LoginPage:
    def __init__(self, url):
        self.url = url

    def describe(self):
        return f"This is the login page at {self.url}"

page = LoginPage("https://www.saucedemo.com")
print(page.describe())

