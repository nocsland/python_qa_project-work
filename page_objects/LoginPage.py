import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    path = '/index.php?route=account/login'

    @allure.step('Найти элемент "input-email"')
    def find_input_email(self):
        self.browser.find_element(By.ID, 'input-email')
        self.logger.info('input_email was found')
        return self

    @allure.step('Найти кнопку "Continue"')
    def find_continue_button(self):
        self.browser.find_element(By.LINK_TEXT, 'Continue')
        self.logger.info('continue button was found')
        return self

    @allure.step('Найти элемент "input-password"')
    def find_input_password(self):
        self.browser.find_element(By.XPATH, '//*[@id="input-password"]')
        self.logger.info('input-password was found')
        return self

    @allure.step('Найти элемент "Forgotten Password"')
    def find_forgotten_password(self):
        self.browser.find_element(By.LINK_TEXT, 'Forgotten Password')
        self.logger.info('Forgotten Password was found')
        return self

    @allure.step('Найти кнопку "login"')
    def find_login_button(self):
        self.browser.find_element(By.XPATH, '//*[@id="form-login"]/button')
        self.logger.info('login button was found')
        return self

    @allure.step('Войти, как пользователь')
    def login_as_customer(self, email, password):
        self.browser.find_element(By.ID, 'input-email').send_keys(email)
        self.browser.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="form-login"]/button').click()
        self.logger.info('logged in')
        return self

    @allure.step('Выйти из УЗ пользователя')
    def logout_as_customer(self):
        self.wait_link_text('Logout')
        self.browser.find_element(By.LINK_TEXT, 'Logout').click()
        self.logger.info('logout done')
        return self
