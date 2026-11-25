from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.click_inventory = page.locator("a[href='/odoo/inventory']")
        self.product_0 = page.locator("//button //span[text()='Products']")
        self.product_1 = page.locator("//a[text()='Products']")
        self.new_product = page.locator("//div //button[text()=' New '] ")
        self.enter_product = page.locator("//div //textarea[@id='name_0'] ")
        self.sales_price = page.locator("#list_price_0")
        self.unit_price = page.locator("div input[id='standard_price_0']")
        self.select_category = page.locator("div input[id='categ_id_0']")
        self.click_category = page.locator("li a[id ='categ_id_0_0_0']")
        self.track = page.locator("div input[id='tracking_1']")
        self.tracking_type = page.locator("//div [@role='menu']//span[@data-choice-index='1'] //div[text()='By Lots']")
        self.reference = page.locator("div input[id='default_code_0']")
        self.save = page.locator("button i[class='fa fa-cloud-upload fa-fw'] ")
        self.warning=page.locator("//span[text()='Missing required fields']")

    def create_product(self, name, sales_price, cost, category_text, reference):
        self.click_inventory.click()
        self.product_0.click()
        self.product_1.click()
        self.new_product.click()

        self.enter_product.fill(name)
        self.sales_price.fill(str(sales_price))
        self.unit_price.fill(str(cost))

        self.select_category.fill(category_text)
        self.click_category.click()

        self.track.click()
        self.tracking_type.click()

        self.reference.fill(reference)
        self.save.click()
    
    def warning_product(self):
        return self.warning