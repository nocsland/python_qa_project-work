import allure

from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    path = '/index.php?route=account/login'

    @allure.step('Найти элемент "input-email"')
    def find_input_email(self):
        self.browser.find_element_by_id('input-email')
        self.logger.info('input_email was found')
        return self

    @allure.step('Найти кнопку "Continue"')
    def find_continue_button(self):
        self.browser.find_element_by_link_text('Continue')
        self.logger.info('continue button was found')
        return self

    @allure.step('Найти элемент "input-password"')
    def find_input_password(self):
        self.browser.find_element_by_xpath('//*[@id="input-password"]')
        self.logger.info('input-password was found')
        return self

    @allure.step('Найти элемент "Forgotten Password"')
    def find_forgotten_password(self):
        self.browser.find_element_by_link_text('Forgotten Password')
        self.logger.info('Forgotten Password was found')
        return self

    @allure.step('Найти кнопку "login"')
    def find_login_button(self):
        self.browser.find_element_by_xpath('//*[@id="content"]//form/input')
        self.logger.info('login button was found')
        return self

    @allure.step('Войти, как пользователь')
    def login_as_customer(self, email, password):
        self.browser.find_element_by_id('input-email').send_keys(email)
        self.browser.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="content"]//form/input').click()
        self.logger.info('logged in')
        return self

    @allure.step('Выйти из УЗ пользователя')
    def logout_as_customer(self):
        self.browser.find_element_by_link_text('Logout').click()
        self.logger.info('logout done')
        return self


