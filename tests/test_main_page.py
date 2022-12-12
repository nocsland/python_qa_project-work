import allure

from db import DbUtility
from page_objects.MainPage import MainPage


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты главной страницы")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка title")
@allure.title("Проверка title главной страницы")
@allure.description("""Тест проверяет title главной страницы""")
@allure.severity(allure.severity_level.CRITICAL)
def test_is_title(browser):
    main_page = MainPage(browser).open()
    main_page.verify_title('Your Store')


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты главной страницы")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка главной страницы")
@allure.title("Поиск элементов на главной странице")
@allure.description("""Тест проверяет наличие элементов на главной странице""")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_el_main(browser):
    main_page = MainPage(browser).open()
    main_page.find_h1_your_store()
    main_page.find_name_search()
    main_page.find_id_cart()
    main_page.find_link_iphone()
    main_page.find_part_link_terms()


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты главной страницы")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка главной страницы")
@allure.title("Добавление нового пользователя")
@allure.description("""Тест проверяет возможность добавить нового пользователя""")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_user(browser):
    main_page = MainPage(browser).open()
    main_page.click_add_user()
    main_page.fill_register_form('Ivan', 'Ivanov', 'test@ya.ru', 'test')
    main_page.click_agree_and_continue()
    main_page.verify_title('My Account')
    DbUtility.delete_test_customer()


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты главной страницы")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка главной страницы")
@allure.title("Переключение валюты")
@allure.description("""Тест проверяет возможность переключить валюту цен и расчетов""")
@allure.severity(allure.severity_level.NORMAL)
def test_switch_currency(browser):
    main_page = MainPage(browser).open()
    main_page.click_switch_currency()
    main_page.wait_element_contains_text('€ Euro')
    main_page.click_to_currency('€ Euro')
    main_page.click_switch_currency()
    main_page.wait_element_contains_text('£ Pound Sterling')
    main_page.click_to_currency('£ Pound Sterling')
    main_page.click_switch_currency()
    main_page.wait_element_contains_text('$ US Dollar')
    main_page.click_to_currency('$ US Dollar')


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты главной страницы")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка главной страницы")
@allure.title("Добавить и удалить товар из корзины")
@allure.description("""Тест проверяет возможность добавить товар в корзину и его удаление из корзины""")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_and_remove_item_to_cart(browser):
    main_page = MainPage(browser).open()
    main_page.add_item_to_cart()
    main_page.wait_css_element('.alert-dismissible')
    main_page.remove_item_from_cart()
