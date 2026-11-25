from playwright.sync_api import Page, expect

class Login:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://133801984-19-0-all.runbot345.odoo.com/web/login"
        self.email=page.locator("#login")
        self.password=page.locator("#password")
        self.login_button=page.locator("//button[text()='Log in']")
        self.warning=page.locator("p[class='alert alert-danger']")
    
    def navigation(self):
        self.page.goto(self.url)
    
    def login_details(self,username,password):
        self.email.fill(username)
        self.password.fill(password)
        self.login_button.click()
    
    def warning_message(self):
        return self.warning