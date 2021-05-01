import pytest
from selenium import webdriver

def test_chek_see_basket_button(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    chek_button = browser.find_element_by_css_selector("button.btn.btn-add-to-basket")

    assert chek_button, "Button not found!!!"