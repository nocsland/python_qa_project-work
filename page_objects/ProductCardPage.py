import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    path = '/index.php?route=product/product&path=57&product_id=49'

    @allure.step('Поиск элемента h1, ожидание загрузки плашек соцсетей')
    def find_h1_product(self):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(.,"Tweet")]')))
        self.browser.find_element_by_xpath('//h1[contains(.,"Samsung Galaxy Tab 10.1")]')
        self.logger.info("element was found")
        return self

    @allure.step('Найти элемент "Add to cart"')
    def find_button_add_to_cart(self):
        self.browser.find_element_by_xpath('//*[@id="button-cart"]')
        self.logger.info("element was found")
        return self

    @allure.step('Найти элемент "input-quantity"')
    def find_input_quantity(self):
        self.browser.find_element_by_id('input-quantity')
        self.logger.info("element was found")
        return self

    @allure.step('Найти и кликнуть ссылку "Write a review"')
    def click_write_a_review(self):
        self.browser.find_element_by_link_text('Write a review').click()
        self.logger.info("Write a review was clicked")
        return self

    @allure.step('Найти вкладку "Description"')
    def find_tab_description(self):
        self.browser.find_element_by_id('tab-description')
        self.logger.info("element was found")
        return self

    @allure.step('Найти и заполнить "Your Name"')
    def fill_name_reviewer(self, name_reviewer):
        self.browser.find_element_by_id('input-name').send_keys(name_reviewer)
        self.logger.info("field 'Your Name' was filled")
        return self

    @allure.step('Найти и заполнить "Your Review"')
    def fill_review(self, review):
        self.browser.find_element_by_id('input-review').send_keys(review)
        self.logger.info("field 'Your Review' was filled")
        return self

    @allure.step('Найти и заполнить рейтинг')
    def click_rating(self):
        self.browser.find_element_by_css_selector('input[value="5"]').click()
        self.logger.info("radio-button was clicked")
        return self

    @allure.step('Кликнуть по "Continue"')
    def click_review_button(self):
        self.browser.find_element_by_id('button-review').click()
        self.logger.info("button 'Continue' was clicked")
        return self
