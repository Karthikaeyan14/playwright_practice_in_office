from playwright.sync_api import Page, expect
import pytest
from page_object_model.login import Login

@pytest.mark.valid_login
def test_valid_login(page:Page):
    login=Login(page)
    login.navigation()
    login.login_details("admin","admin")

@pytest.mark.invalid_login
def test_invalid_login(page:Page):
    login=Login(page)
    login.navigation()
    login.login_details("admin","ad")
    a=login.warning_message() 
    print(a.inner_text())
    expect(a).to_contain_text("Wrong login/password")