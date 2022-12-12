import allure

from page_objects.CatalogPage import CatalogPage


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы каталога")
@allure.epic("Тестирование типового магазина")
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


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты страницы каталога")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка каталога")
@allure.title("Добавление товаров в сравнение")
@allure.description("""Тест проверяет возможность добавить товары в лист сравнения""")
@allure.severity(allure.severity_level.NORMAL)
def test_add_items_to_compare(browser):
    catalog_page = CatalogPage(browser).open()
    catalog_page.add_compare_list(1)
    catalog_page.wait_css_element('.alert-dismissible')
    catalog_page.add_compare_list(2)
    catalog_page.wait_css_element('.alert-dismissible')
    catalog_page.open_compare_list()
    catalog_page.verify_title('Product Comparison')
    catalog_page.wait_element_contains_text("Apple Cinema")
    catalog_page.wait_element_contains_text("Canon EOS")
