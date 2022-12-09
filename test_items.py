import time
from selenium.webdriver.common.by import By



class TestIsButton:

    def test_button_add_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_displayed(), 'Кнопки нет'
