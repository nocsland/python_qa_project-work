import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    path = '/'

    @allure.step('Найти заголовок типа h1')
    def find_h1_your_store(self):
        self.logger.info('element was found')
        return self.browser.find_element(By.XPATH, '//*[@id="logo"]/a/img')

    @allure.step('Найти элемент "Search"')
    def find_name_search(self):
        self.logger.info('element was found')
        return self.browser.find_element(By.NAME, 'search')

    @allure.step('Найти элемент "Cart"')
    def find_id_cart(self):
        self.logger.info('element was found')
        return self.browser.find_element(By.ID, 'header-cart')

    @allure.step('Найти ссылку "iPhone"')
    def find_link_iphone(self):
        self.logger.info('element was found')
        return self.browser.find_element(By.LINK_TEXT, 'iPhone')

    @allure.step('Найти элемент "Terms & Conditions"')
    def find_part_link_terms(self):
        self.logger.info('element was found')
        return self.browser.find_elements(By.PARTIAL_LINK_TEXT, 'Terms & Cond')

    @allure.step('Добавить товар с главной страницы, в корзину')
    def add_item_to_cart(self):
        self.browser.find_element(By.XPATH, '//img[@alt="MacBook"]').click()
        self.browser.find_element(By.ID, 'button-cart').click()
        self.logger.info('added item to cart')
        return self

    @allure.step('Удалить товар из корзины')
    def remove_item_from_cart(self):
        self.browser.find_element(By.ID, 'header-cart').click()
        self.browser.find_element(By.XPATH, '//button[@title="Remove"]').click()
        self.browser.find_elements(By.PARTIAL_LINK_TEXT, '0 item(s) - $0.00')
        self.logger.info('removed item from cart')
        return self
