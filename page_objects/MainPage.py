import allure

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    path = '/'

    @allure.step('Найти заголовок типа h1')
    def find_h1_your_store(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_xpath('//*[@id="logo"]/h1/a')

    @allure.step('Найти элемент "Search"')
    def find_name_search(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_name('search')

    @allure.step('Найти элемент "Cart"')
    def find_id_cart(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_id('cart')

    @allure.step('Найти ссылку "iPhone"')
    def find_link_iphone(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_link_text('iPhone')

    @allure.step('Найти элемент "Terms & Conditions"')
    def find_part_link_terms(self):
        self.logger.info('element was found')
        return self.browser.find_elements_by_partial_link_text('Terms & Cond')

    @allure.step('Добавить товар с главной страницы, в корзину')
    def add_item_to_cart(self):
        self.browser.find_element_by_xpath('//img[@alt="MacBook"]').click()
        self.browser.find_element_by_id('button-cart').click()
        self.logger.info('added item to cart')
        return self

    @allure.step('Удалить товар из корзины')
    def remove_item_from_cart(self):
        self.browser.find_element_by_id('cart-total').click()
        self.browser.find_element_by_xpath('//button[@title="Remove"]').click()
        self.browser.find_elements_by_partial_link_text('0 item(s) - $0.00')
        self.logger.info('removed item from cart')
        return self
