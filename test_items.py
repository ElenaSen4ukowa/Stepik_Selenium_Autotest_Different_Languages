import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]

@pytest.mark.parametrize('link', links)
def test_guest_should_see_basket_button(browser, link):
    browser.get(link)

    # для визуальной проверки языка интерфейса 
    # time.sleep(30)

    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, 'no such button!'
