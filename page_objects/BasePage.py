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
        WebDriverWait(self.browser, 5).until(EC.title_is(title))
        assert self.browser.title == title
        self.logger.info('title was verified')
        return self

    @allure.step('Вход в админ панель')
    def login(self, login, password):
        self.browser.find_element(By.NAME, 'username').clear()
        self.browser.find_element(By.NAME, 'username').send_keys(login)
        self.browser.find_element(By.ID, 'input-password').clear()
        self.browser.find_element(By.ID, 'input-password').send_keys(password)
        self.browser.find_element(By.XPATH, '//button[contains(.," Login")]').click()
        self.logger.info("login completed")
        return self

    @allure.step('Переключение окна')
    def switch_to_alert_and_ok(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        self.logger.info('switch alert is ok')
        return self

    @allure.step('Ожидание видимости ccылки')
    def wait_link_text(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))
        self.logger.info('text link is visible')
        return self

    @allure.step('Ожидание видимости css элемента')
    def wait_css_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.logger.info('css element is visible')
        return self

    @allure.step('Ожидание видимости элемента')
    def wait_element_is_visible(self, locator, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((locator, selector)))
        self.logger.info('element is visible')
        return self

    @allure.step('Ожидание видимости всех элементов')
    def wait_all_elements_is_visible(self, locator, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_all_elements_located((locator, selector)))
        self.logger.info('elements is visible')
        return self

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable_element(self, locator, selector):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_clickable((locator, selector)))
        self.logger.info('element is clickable')
        return

    @allure.step('Ожидание выбора элемента')
    def wait_selected_element(self, locator, selector):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_selected((locator, selector)))
        self.logger.info('element is selected')
        return self

    @allure.step('Ожидание видимости текста элемента')
    def wait_element_contains_text(self, text):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(),'{text}')]")))
        self.logger.info('element contains text')
        return self

    @allure.step('Ожидание видимости части ссылки')
    def wait_partial_link_text(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))
        self.logger.info('partial link is visible')
        return self

    @allure.step('Переключение валюты')
    def click_switch_currency(self):
        self.browser.find_element(By.ID, 'form-currency').click()
        self.logger.info('switch currency menu was called')
        return self

    @allure.step('Выбор валюты')
    def click_to_currency(self, currency):
        self.browser.find_element(By.XPATH, f'//a[contains(text(),"{currency}")]').click()
        self.logger.info('currency was switched')
        return self

    @allure.step('Открыть страницу панели администратора')
    def open_admin(self):
        self.browser.get(self.url + '/administration/index.php?route=common/')
        return self

    @allure.step('Перейти на страницу "Customers"')
    def goto_all_customers(self):
        self.wait_element_is_visible(By.XPATH, '//*[@id="menu-customer"]/a')
        self.browser.find_element(By.XPATH, '//*[@id="menu-customer"]/a').click()
        self.browser.find_elements(By.XPATH, '//a[contains(text(),"Customers")]')[1].click()
        self.verify_title('Customers')
        self.logger.info('navigated to all customers')
        return self

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.browser.get(self.url + '/')
        return self

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.browser.get(self.url + '/index.php?route=account/login')
        return self

    @allure.step('Найти и нажать "Register"')
    def click_add_user(self):
        self.browser.find_element(By.CSS_SELECTOR, '.fa-user').click()
        self.logger.info('dropdown menu was clicked')
        self.browser.find_element(By.LINK_TEXT, 'Register').click()
        self.logger.info('Register was clicked')
        return self

    @allure.step('Заполнить обязательные поля формы регистрации пользователя')
    def fill_register_form(self, f_name, l_name, email, password):
        self.browser.find_element(By.ID, 'input-firstname').clear()
        self.browser.find_element(By.ID, 'input-firstname').send_keys(f_name)
        self.browser.find_element(By.ID, 'input-lastname').clear()
        self.browser.find_element(By.ID, 'input-lastname').send_keys(l_name)
        self.browser.find_element(By.ID, 'input-email').clear()
        self.browser.find_element(By.ID, 'input-email').send_keys(email)
        self.browser.find_element(By.ID, 'input-password').clear()
        self.browser.find_element(By.ID, 'input-password').send_keys(password)
        self.logger.info('all fields register form was filled')
        return self

    @allure.step('Найти и нажать "Agree" и "Continue"')
    def click_agree_and_continue(self):
        self.browser.find_element(By.NAME, 'agree').click()
        self.browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
        self.wait_link_text('Continue')
        self.browser.find_element(By.LINK_TEXT, 'Continue').click()
        self.logger.info('agree and continue was clicked')
        return self
