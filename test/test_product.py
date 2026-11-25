from playwright.sync_api import Page, expect
import pytest
from page_object_model.product_creation import InventoryPage
from page_object_model.login import Login

def test_product(page:Page):
    login=Login(page)
    login.navigation()
    login.sign_click()
    login.login_details('admin','admin')
    inventory=InventoryPage(page)
    inventory.create_product("Test_product_1","15","10","Clothes","REF001")
 

def test_invalid_product(page:Page):
    login=Login(page)
    login.navigation()
    login.sign_click()
    login.login_details('admin','admin')
    inventory=InventoryPage(page)
    inventory.create_product("","15","10","Clothes","REF001")
    print_the_value=inventory.warning_product()
    print(print_the_value.inner_text())# 
    #expect(inventory.warning_product()).to_have_text("missing required fields")
    expect(inventory.warning_product()).to_be_visible()
