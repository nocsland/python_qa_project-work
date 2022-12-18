import allure

from db import DbUtility
from page_objects.AdminPage import AdminPage


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы администратора")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка страницы администратора")
@allure.title("Поиск элементов на странице администратора")
@allure.description("""Тест проверяет наличие элементов на странице админки""")
@allure.severity(allure.severity_level.NORMAL)
def test_find_el_on_admin_page(browser):
    admin_page = AdminPage(browser).open()
    admin_page.find_logo_open_cart()
    admin_page.find_input_username()
    admin_page.find_h1_in_form()
    admin_page.find_input_password()
    admin_page.find_login_button()


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы администратора")
@allure.feature("Проверка страницы администратора")
@allure.epic("Тестирование типового магазина")
@allure.title("Добавление продукта администратором")
@allure.description("Тест проверяет возможность добавить новый продукт")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product(browser):
    DbUtility.delete_test_product()
    admin_page = AdminPage(browser).open()
    admin_page.login('user', 'bitnami')
    admin_page.verify_title('Dashboard')
    admin_page.goto_all_products()
    admin_page.verify_title('Products')
    admin_page.click_add_product()
    admin_page.fill_general_form_product('test', 'test')
    admin_page.goto_data_tab()
    admin_page.fill_data_tab_product('test')
    admin_page.goto_seo_tab()
    admin_page.fill_seo_tab_product("test")
    admin_page.click_save_product()
    admin_page.wait_css_element('.alert-dismissible')


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы администратора")
@allure.feature("Проверка страницы администратора")
@allure.epic("Тестирование типового магазина")
@allure.title("Удаление продукта администратором")
@allure.description("Тест проверяет возможность удалить продукт")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product(browser):
    admin_page = AdminPage(browser).open()
    admin_page.login('user', 'bitnami')
    admin_page.goto_all_products()
    admin_page.verify_title('Products')
    admin_page.find_and_delete_product()
    admin_page.switch_to_alert_and_ok()
    admin_page.wait_css_element('.alert-dismissible')


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы администратора")
@allure.feature("Проверка страницы администратора")
@allure.epic("Тестирование типового магазина")
@allure.title("Удаление пользователя администратором")
@allure.description("Тест проверяет возможность удалить пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_customer(browser):
    DbUtility.insert_test_customer()
    admin_page = AdminPage(browser).open()
    admin_page.login('user', 'bitnami')
    admin_page.goto_all_customers()
    admin_page.delete_customer()
