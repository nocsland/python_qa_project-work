import allure

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    path = '/admin/'

    @allure.step('Поиск логотипа')
    def find_logo_open_cart(self):
        self.browser.find_element_by_xpath("//img[@alt='OpenCart']")
        self.logger.info("element was found")
        return self

    @allure.step('Поиск поля ввода "username"')
    def find_input_username(self):
        self.browser.find_element_by_name('username')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск заголовка типа h1')
    def find_h1_in_form(self):
        self.browser.find_element_by_xpath('//h1[contains(.," Please enter your login details.")]')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск поля ввода "password"')
    def find_input_password(self):
        self.browser.find_element_by_id('input-password')
        self.logger.info("element was found")
        return self

    @allure.step('Поиск кнопки "Login"')
    def find_login_button(self):
        self.browser.find_element_by_xpath('//button[contains(.," Login")]')
        self.logger.info("element was found")
        return self

    @allure.step('Переход на страницу "Products"')
    def goto_all_products(self):
        self.browser.find_element_by_id('menu-catalog').click()
        self.browser.find_element_by_xpath('//a[contains(text(),"Products")]').click()
        self.logger.info('navigated to the all products page')
        return self

    @allure.step('Нажать на кнопку "Add new"')
    def click_add_product(self):
        self.browser.find_element_by_css_selector('.fa-plus').click()
        self.logger.info('clicked add')
        return self

    @allure.step('Заполнить обязательные поля формы добавления товара на вкладке "General"')
    def fill_general_form_product(self, name, title):
        self.browser.find_element_by_id('input-name1').send_keys(name)
        self.browser.find_element_by_id('input-meta-title1').send_keys(title)
        self.logger.info('the name and title fields are filled')
        return self

    @allure.step('Переход на вкладку "Data" формы добавления товара')
    def goto_data_tab(self):
        self.browser.find_element_by_link_text('Data').click()
        self.logger.info('navigated to the data tab')
        return self

    @allure.step('Заполнить поле "Model" на вкладке "Data"')
    def fill_data_tab_product(self, model):
        self.browser.find_element_by_id('input-model').send_keys(model)
        self.logger.info('the model field is filled')
        return self

    @allure.step('Нажать кнопку "Save"')
    def click_save_product(self):
        self.browser.find_element_by_css_selector('.fa-save').click()
        self.logger.info('product was saved')
        return self

    @allure.step('Найти и удалить товар из каталога')
    def find_and_delete_product(self):
        self.browser.find_element_by_xpath('//tr/td[3][contains(text(),"test")]/..//input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
        self.logger.info('product was deleted')
        return self

    @allure.step('Удалить УЗ пользователя')
    def delete_customer(self):
        self.browser.find_element_by_xpath('//tr/td[2][contains(text(),"Ivan Ivanov")]/..//input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
        self.switch_to_alert_and_ok()
        self.wait_css_element('.fa-check-circle')
        self.logger.info('customer was deleted')
        return self
