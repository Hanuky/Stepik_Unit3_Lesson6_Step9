import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestProductPage():
    def element_exist(self, selector, browser):
        try:
            x = browser.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException:
            return False    

    def test_chek_see_basket_button(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        chek_button = self.element_exist("button.btn.btn-add-to-basket", browser)
        assert chek_button, "Button not found!!!"