import pytest
import re
from playwright.sync_api import Page, expect





def test_login(page:Page):
    username=page.locator("#userEmail")
    password=page.locator("#userPassword")
    print("The user login")
    #page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/auth/login")
    username.type("vijay1412@gmail.com")
    password.type("Vijaykumar@14")
    page.locator("#login").click()
    
    expect(username).to_have_value("vijay1412@gmail.com")
    expect(password).to_have_value("Vijaykumar@14")
    
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    
    page.pause()
    
# to_have_text() - MUST match the whole sentence
# to_contain_text() - ONLY needs a matching piece
def test_login_2(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    admin=page.locator("//span[text()=' User']")
    conform_popup=page.locator("#okayBtn")
    alter_popup=page.locator("//div[@style='display: block;']")
    sign_button=page.locator("#signInBtn")
    admin.click()
    expect(admin).to_be_checked()
    
    
    popup=page.locator(".modal-body p")
    expect(popup).to_have_text("You will be limited to only fewer functionalities of the app. Proceed?") 
    
    #print(popup.text_content())
    conform_popup.click()
    sign_button.click()
    expect(alter_popup).to_be_visible()
    
    
    #print(alter_popup.text_content())

    
  