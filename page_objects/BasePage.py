import logging
import allure


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    path = None

    def __init__(self, browser):
        self.browser = browser
        self.url = browser.url
        self.logger = logging.getLogger(type(self).__name__)

    def open(self):
        self.browser.get(self.url + self.path)
        self.logger.info('browser was opened')
        return self

    @allure.step('Проверка title')
    def verify_title(self, title):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.title_is(title))
        assert self.browser.title == title
        self.logger.info('title was verified')
        return self

    @allure.step('Вход в админ панель')
    def login(self, login, password):
        self.browser.find_element_by_name('username').clear()
        self.browser.find_element_by_name('username').send_keys(login)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_xpath('//button[contains(.," Login")]').click()
        self.logger.info("login completed")
        return self

    @allure.step('Переключение окна')
    def switch_to_alert_and_ok(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        self.logger.info('switch alert is ok')
        return self

    @allure.step('Ожидание видимости элемента')
    def wait_css_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.logger.info('element is visible')
        return self

    @allure.step('Переключение валюты')
    def click_switch_currency(self):
        self.browser.find_element_by_id('form-currency').click()
        self.logger.info('switch currency menu was called')
        return self

    @allure.step('Выбор валюты')
    def click_to_currency(self, currency):
        self.browser.find_element_by_css_selector(f'button[name="{currency}"]').click()
        self.logger.info('currency was switched')
        return self

    @allure.step('Открыть страницу админ панели')
    def open_admin(self):
        self.browser.get(self.url + '/admin/')
        return self
