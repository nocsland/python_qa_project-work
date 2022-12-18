import allure

from db import DbUtility
from page_objects.LoginPage import LoginPage


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы авторизации")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка наличия элементов на странице логина")
@allure.title("Поиск элементов на странице логина")
@allure.description("""Тест проверяет наличие элементов на странице логина""")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_elements_login_page(browser):
    login_page = LoginPage(browser).open()
    login_page.find_input_email()
    login_page.find_continue_button()
    login_page.find_input_password()
    login_page.find_forgotten_password()
    login_page.find_login_button()


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы авторизации")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка возможности входа и выхода пользователя")
@allure.title("Вход/выход на странице авторизации")
@allure.description("""Тест проверяет возможность входа и выхода, как пользователь на странице авторизации""")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_as_customer(browser):
    # pytest.skip('Причина пропуска теста')
    DbUtility.insert_test_customer()
    login_page = LoginPage(browser).open()
    login_page.login_as_customer('test@ya.ru', 'test')
    login_page.logout_as_customer()
    login_page.verify_title('Account Logout')
    DbUtility.delete_test_customer()
