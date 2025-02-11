import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add__to_basket_button_is_exist(browser):
    browser.get(link)
    add_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))

    assert add_button.is_enabled(), "Add to basket button is not clickable"
    time.sleep(5)