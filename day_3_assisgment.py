class InventoryPage:
    def __init__(self, url, page_name):
        self.url = url
        self.page_name = page_name

    def describe(self):
        return f"This is the {self.page_name} at {self.url}"

page = InventoryPage("https://saucelabs.com/", "Inventory Page")
print(page.describe())      