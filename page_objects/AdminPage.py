import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    path = '/administration/'

    @allure.step('Поиск логотипа')
    def find_logo_open_cart(self):
        self.browser.find_element(By.XPATH, "//img[@alt='OpenCart']")
        self.logger.info("element was found")
        return self

    @allure.step('Поиск поля ввода "username"')
    def find_input_username(self):
        self.browser.find_element(By.NAME, 'username')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск заголовка типа h1')
    def find_h1_in_form(self):
        self.browser.find_element(By.XPATH, '//*[contains(.," Please enter your login details.")]')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск поля ввода "password"')
    def find_input_password(self):
        self.browser.find_element(By.ID, 'input-password')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск кнопки "Login"')
    def find_login_button(self):
        self.browser.find_element(By.XPATH, '//button[contains(.," Login")]')
        self.logger.info("element was found")
        return self

    @allure.step('Переход на страницу "Products"')
    def goto_all_products(self):
        self.wait_clickable_element(By.ID, 'menu-catalog')
        element = self.browser.find_element(By.ID, 'menu-catalog').click()
        # self.browser.execute_script("arguments[0].click();", element)
        self.browser.find_element(By.XPATH, '//a[contains(text(),"Products")]').click()
        self.logger.info('navigated to the all products page')
        return self

    @allure.step('Нажать на кнопку "Add new"')
    def click_add_product(self):
        self.browser.find_element(By.CSS_SELECTOR, '.fa-plus').click()
        self.logger.info('clicked add')
        return self

    @allure.step('Заполнить обязательные поля формы добавления товара на вкладке "General"')
    def fill_general_form_product(self, name, title):
        self.browser.find_element(By.ID, 'input-name-1').send_keys(name)
        self.browser.find_element(By.ID, 'input-meta-title-1').send_keys(title)
        self.logger.info('the name and title fields are filled')
        return self

    @allure.step('Переход на вкладку "Data" формы добавления товара')
    def goto_data_tab(self):
        self.browser.find_element(By.LINK_TEXT, 'Data').click()
        self.logger.info('navigated to the data tab')
        return self

    @allure.step('Переход на вкладку "SEO" формы добавления товара')
    def goto_seo_tab(self):
        self.browser.find_element(By.LINK_TEXT, 'SEO').click()
        self.logger.info('navigated to the seo tab')
        return self

    @allure.step('Заполнить поле "Model" на вкладке "Data"')
    def fill_data_tab_product(self, model):
        self.browser.find_element(By.ID, 'input-model').send_keys(model)
        self.logger.info('the model field is filled')
        return self

    @allure.step('Заполнить поля на вкладке "SEO"')
    def fill_seo_tab_product(self, keyword):
        self.browser.find_element(By.ID, 'input-keyword-0-1').send_keys(keyword)
        self.logger.info('the seo fields is filled')
        return self

    @allure.step('Нажать кнопку "Save"')
    def click_save_product(self):
        self.browser.find_element(By.CSS_SELECTOR, '.fa-floppy-disk').click()
        self.logger.info('product was saved')
        return self

    @allure.step('Найти и удалить товар из каталога')
    def find_and_delete_product(self):
        self.browser.find_element(By.ID, 'input-name').send_keys("test")
        self.browser.find_element(By.ID, 'button-filter').click()
        self.wait_element_is_visible(By.CSS_SELECTOR, 'input[type="checkbox"]:last-of-type')
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]:last-of-type').click()
        self.browser.find_element(By.CSS_SELECTOR, '.fa-trash-can').click()
        self.logger.info('product was deleted')
        return self

    @allure.step('Удалить УЗ пользователя')
    def delete_customer(self):
        self.wait_element_is_visible(By.XPATH, '//tr/td[2][contains(text(),"Ivan Ivanov")]/..//input')
        self.browser.find_element(By.XPATH, '//tr/td[2][contains(text(),"Ivan Ivanov")]/..//input').click()
        self.browser.find_element(By.CSS_SELECTOR, '.fa-trash-can').click()
        self.switch_to_alert_and_ok()
        self.wait_css_element('.alert-dismissible')
        self.logger.info('customer was deleted')
        return self
