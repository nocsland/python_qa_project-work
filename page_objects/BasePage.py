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

    @allure.step('Открыть страницу')
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

    @allure.step('Ожидание видимости css элемента')
    def wait_css_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.logger.info('css element is visible')
        return self

    @allure.step('Ожидание видимости части ссылки')
    def wait_partial_link_text(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))
        self.logger.info('partial link is visible')
        return self

    @allure.step('Ожидание видимости xpath элемента')
    def wait_xpath_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        self.logger.info('XPATH is visible')
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

    @allure.step('Открыть страницу панели администратора')
    def open_admin(self):
        self.browser.get(self.url + '/admin/')
        return self

    @allure.step('Перейти на страницу "Customers"')
    def goto_all_customers(self):
        self.browser.find_element_by_xpath('//*[@id="menu-customer"]/a').click()
        self.browser.find_elements_by_xpath('//a[contains(text(),"Customers")]')[1].click()
        self.verify_title('Customers')
        self.logger.info('navigated to all customers')
        return self

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.browser.get(self.url + '/')
        return self

    @allure.step('Найти и нажать "Register"')
    def click_add_user(self):
        self.browser.find_element_by_css_selector('.fa-user').click()
        self.logger.info('dropdown menu was clicked')
        self.browser.find_element_by_link_text('Register').click()
        self.logger.info('Register was clicked')
        return self

    @allure.step('Найти и нажать "Login"')
    def click_login_user_top(self):
        self.browser.find_element_by_css_selector('.fa-user').click()
        self.logger.info('dropdown menu was clicked')
        self.browser.find_element_by_link_text('Login').click()
        self.logger.info('Login was clicked')
        return self

    @allure.step('Заполнить обязательные поля формы регистрации пользователя')
    def fill_register_form(self, f_name, l_name, email, phone, password):
        self.browser.find_element_by_id('input-firstname').clear()
        self.browser.find_element_by_id('input-firstname').send_keys(f_name)
        self.browser.find_element_by_id('input-lastname').clear()
        self.browser.find_element_by_id('input-lastname').send_keys(l_name)
        self.browser.find_element_by_id('input-email').clear()
        self.browser.find_element_by_id('input-email').send_keys(email)
        self.browser.find_element_by_id('input-telephone').clear()
        self.browser.find_element_by_id('input-telephone').send_keys(phone)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_id('input-confirm').clear()
        self.browser.find_element_by_id('input-confirm').send_keys(password)
        self.logger.info('all fields register form was filled')
        return self

    @allure.step('Найти и нажать "Agree" и "Continue"')
    def click_agree_and_continue(self):
        self.browser.find_element_by_name('agree').click()
        self.browser.find_element_by_css_selector('.btn-primary').click()
        self.browser.find_element_by_link_text('Continue').click()
        self.logger.info('agree and continue was clicked')
        return self

    @allure.step('Удалить УЗ пользователя Ivan Ivanov')
    def delete_customer(self):
        self.browser.find_element_by_xpath('//tr/td[2][contains(text(),"Ivan Ivanov")]/..//input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
        self.switch_to_alert_and_ok()
        self.wait_css_element('.fa-check-circle')
        self.logger.info('customer was deleted')
        return self
