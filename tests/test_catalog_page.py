import allure

from page_objects.CatalogPage import CatalogPage


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты страницы каталога")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка каталога")
@allure.title("Поиск элементов на странице каталога")
@allure.description("""Тест проверяет наличие элементов на странице каталога""")
@allure.severity(allure.severity_level.NORMAL)
def test_find_el_catalog(browser):
    catalog_page = CatalogPage(browser).open()
    catalog_page.find_top_menu()
    catalog_page.find_left_menu()
    catalog_page.find_link_product_compare()
    catalog_page.find_class_input_group()
    catalog_page.find_search_button()


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты страницы каталога")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка каталога")
@allure.title("Добавление товаров в сравнение")
@allure.description("""Тест проверяет возможность добавить товары в лист сравнения""")
@allure.severity(allure.severity_level.NORMAL)
def test_add_items_to_compare(browser):
    catalog_page = CatalogPage(browser).open()
    catalog_page.add_compare_list(6)
    catalog_page.wait_partial_link_text('Product Compare (1)')
    catalog_page.add_compare_list(7)
    catalog_page.wait_partial_link_text('Product Compare (2)')
    catalog_page.open_compare_list()
    catalog_page.verify_title('Product Comparison')
