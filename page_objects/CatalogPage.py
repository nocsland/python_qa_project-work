import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    path = '/index.php?route=product/category&path=20'

    @allure.step('Найти элемент "top div"')
    def find_top_menu(self):
        self.browser.find_element(By.CSS_SELECTOR, '#top > div.container')
        self.logger.info("top div was found")
        return self

    @allure.step('Найти элемент "column-left"')
    def find_left_menu(self):
        self.browser.find_element(By.ID, 'column-left')
        self.logger.info("left column was found")
        return self

    @allure.step('Найти элемент "Product Compare"')
    def find_link_product_compare(self):
        self.browser.find_element(By.ID, 'compare-total')
        self.logger.info("Product Compare was found")
        return self

    @allure.step('Найти элемент "input-group"')
    def find_class_input_group(self):
        self.browser.find_element(By.CLASS_NAME, 'input-group')
        self.logger.info("class input-group was found")
        return self

    @allure.step('Найти кнопку "search"')
    def find_search_button(self):
        self.browser.find_element(By.XPATH, '//*[@id="search"]/button')
        self.logger.info("search button was found")
        return self

    @allure.step('Добавить в лист сравнения товары')
    def add_compare_list(self, position):
        self.wait_all_elements_is_visible(By.CSS_SELECTOR, '.fa-arrow-right-arrow-left')
        element = self.browser.find_elements(By.CSS_SELECTOR, '.fa-arrow-right-arrow-left')[position]
        self.browser.execute_script("arguments[0].click();", element)
        self.logger.info("add to compare list")
        return self

    @allure.step('Открыть лист сравнения')
    def open_compare_list(self):
        self.browser.find_element(By.ID, 'compare-total').click()
        self.logger.info("compare list opened")
        return self
