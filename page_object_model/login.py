from playwright.sync_api import Page, expect

class Login:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://133806330-19-0-all.runbot358.odoo.com/"
        self.sign_in=page.locator("//a[@class='o_nav_link_btn nav-link border px-3']")
        self.email=page.locator("#login")
        self.password=page.locator("#password")
        self.login_button=page.locator("//button[text()='Log in']")
        self.warning=page.locator("p[class='alert alert-danger']")
    
    def navigation(self):
        self.page.goto(self.url)
    
    def sign_click(self):
        self.sign_in.click()
    
    def login_details(self,username,password):
        self.email.fill(username)
        self.password.fill(password)
        self.login_button.click()
    
    def warning_message(self):
        return self.warning