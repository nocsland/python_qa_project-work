import logging
import time

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

    def verify_title(self, title):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.title_is(title))
        assert self.browser.title == title
        self.logger.info('title was verified')
        return self

    def login(self, login, password):
        self.browser.find_element_by_name('username').clear()
        self.browser.find_element_by_name('username').send_keys(login)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_xpath('//button[contains(.," Login")]').click()
        self.logger.info("login completed")
        return self

    def switch_to_alert_and_ok(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        self.logger.info('switch alert is ok')
        return self

    def wait_css_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.logger.info('element is visible')
        return self

    def click_switch_currency(self):
        self.browser.find_element_by_id('form-currency').click()
        self.logger.info('switch currency menu was called')
        return self

    def click_to_currency(self, currency):
        self.browser.find_element_by_css_selector(f'button[name="{currency}"]').click()
        self.logger.info('currency was switched')
        return self

    def delete_customer(self):
        self.browser.find_element_by_xpath('//tr/td[2][contains(text(),"Ivan Ivanov")]/..//input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
        self.switch_to_alert_and_ok()
        self.wait_css_element('.fa-check-circle')
        self.logger.info('customer was deleted')
        return self

    def open_admin(self):
        self.browser.get(self.url + '/admin/')
        return self

    def goto_all_customers(self):
        self.browser.find_element_by_xpath('//*[@id="menu-customer"]/a').click()
        self.browser.find_elements_by_xpath('//a[contains(text(),"Customers")]')[1].click()
        self.verify_title('Customers')
        self.logger.info('navigated to all customers')
        return self
