import allure

from page_objects.ProductCardPage import ProductCardPage


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты карточки товара")
@allure.sub_suite("Поиск элементов на странице карточки товара")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка карточки товара")
@allure.title("Поиск элементов на странице карточки товара")
@allure.description("""Тест проверяет наличие элементов на странице карточки товара""")
@allure.severity(allure.severity_level.NORMAL)
def test_find_elements_on_product_card(browser):
    product_card_page = ProductCardPage(browser).open()
    product_card_page.find_h1_product()
    product_card_page.find_button_add_to_cart()
    product_card_page.find_input_quantity()
    product_card_page.find_tab_description()


@allure.parent_suite("Автоматизация тестирования типового магазина")
@allure.suite("Тесты карточки товара")
@allure.sub_suite("Создание отзыва о товаре")
@allure.epic("Тестирование типового магазина")
@allure.feature("Проверка карточки товара")
@allure.title("Создание отзыва о товаре")
@allure.description("""Тест проверяет возможность создать отзыв на странице карточки товара""")
@allure.severity(allure.severity_level.NORMAL)
def test_write_review_product_card(browser):
    product_card_page = ProductCardPage(browser).open()
    product_card_page.click_write_a_review()
    product_card_page.fill_name_reviewer('reviewer')
    product_card_page.fill_review('1234567890123456789012345(25)')
    product_card_page.click_rating()
    product_card_page.click_review_button()
    product_card_page.wait_css_element('.alert-dismissible')
