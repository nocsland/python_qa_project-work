import datetime
import logging

import mysql.connector as mariadb
from mysql.connector import Error

connection = mariadb.connect(user='bn_opencart', password='', database='bitnami_opencart', host='192.168.1.38',
                             port='3306')
logging.info('Подключение к базе данных выполнено успешно')


def execute_query(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
    except Error as err:
        logging.error("При выполнении запроса произошла ошибка: %s", err)


def get_all_customers():
    query = "select * from oc_customer;"
    execute_query(query)


def insert_test_customer():
    now = datetime.datetime.now()

    query = "insert into oc_customer(customer_group_id, language_id, telephone, custom_field, ip, status, safe, token," \
            " code, date_added,firstname, lastname, email, password)values(1, 1, '', '', '192.168.1.34', 1, 0, '', ''," \
            f" '{now}', 'Ivan', 'Ivanov', 'test@ya.ru', '$2y$10$08SKVb11HmMUEoO3ZKJX3.J5rfjVWrnAve0jDY4hW1YGAnNkfHPUi')"
    execute_query(query)
    connection.commit()
    logging.info("Тестовый пользователь успешно добавлен")


def delete_test_customer():
    query = "delete from oc_customer where email = 'test@ya.ru'"
    execute_query(query)
    connection.commit()
    logging.info("Тестовый пользователь успешно удален")


def delete_test_product():
    query = "delete from oc_product where model = 'test'"
    execute_query(query)
    connection.commit()
    logging.info("Тестовый продукт успешно удален")
    query = "delete from oc_product_description where name = 'test'"
    execute_query(query)
    connection.commit()
    logging.info("Описание тестового продукта успешно удалено")
    query = "delete from oc_seo_url where keyword = 'test'"
    execute_query(query)
    connection.commit()
    logging.info("SEO информация о тестовом продукте успешно удалена")
