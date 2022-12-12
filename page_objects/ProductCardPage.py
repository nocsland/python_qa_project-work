import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    path = '/index.php?route=product/product&path=57&product_id=49'

    @allure.step('Поиск элемента h1, ожидание загрузки плашек соцсетей')
    def find_h1_product(self):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(.,"10hours of video-playback time.")]')))
        self.browser.find_element(By.XPATH, '//h1[contains(.,"Samsung Galaxy Tab 10.1")]')
        self.logger.info("element was found")
        return self

    @allure.step('Найти элемент "Add to cart"')
    def find_button_add_to_cart(self):
        self.browser.find_element(By.XPATH, '//*[@id="button-cart"]')
        self.logger.info("element was found")
        return self

    @allure.step('Найти элемент "input-quantity"')
    def find_input_quantity(self):
        self.browser.find_element(By.ID, 'input-quantity')
        self.logger.info("element was found")
        return self

    @allure.step('Найти и кликнуть ссылку "Write a review"')
    def click_write_a_review(self):
        self.browser.find_element(By.LINK_TEXT, 'Write a review').click()
        self.logger.info("Write a review was clicked")
        return self

    @allure.step('Найти вкладку "Description"')
    def find_tab_description(self):
        self.browser.find_element(By.ID, 'tab-description')
        self.logger.info("element was found")
        return self

    @allure.step('Найти и заполнить "Your Name"')
    def fill_name_reviewer(self, name_reviewer):
        self.wait_element_is_visible(By.ID, 'input-name')
        self.browser.find_element(By.ID, 'input-name').send_keys(name_reviewer)
        self.logger.info("field 'Your Name' was filled")
        return self

    @allure.step('Найти и заполнить "Your Review"')
    def fill_review(self, review):
        self.browser.find_element(By.ID, 'input-text').send_keys(review)
        self.logger.info("field 'Your Review' was filled")
        return self

    @allure.step('Найти и заполнить рейтинг')
    def click_rating(self):
        self.wait_clickable_element(By.CSS_SELECTOR, 'input[value="5"]')
        self.browser.find_element(By.CSS_SELECTOR, 'input[value="5"]').send_keys(Keys.SPACE)
        self.logger.info("radio-button was clicked")
        return self

    @allure.step('Кликнуть по "Continue"')
    def click_review_button(self):
        self.wait_clickable_element(By.ID, 'button-review')
        self.browser.find_element(By.ID, 'button-review').send_keys(Keys.ENTER)
        self.logger.info("button 'Continue' was clicked")
        return self
