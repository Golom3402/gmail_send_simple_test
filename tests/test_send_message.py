# -*- coding: utf-8 -*-
import allure
import pytest
from page_objects.gmail_main import MainPage
from data.message_test_data import constant as test_data_set




@pytest.mark.parametrize("message", test_data_set, ids=[repr(x) for x in test_data_set])
def test_send_message_positive(app, message):
    """
    1 открытие формы составления письма (нажать на кнопку "новое")
    2 ввод значений адресата, темы, тела письма (заполнение формы "новое сообщение")
    3 отправка сообщения (нажать кнопку "отправить")

    4 переход на вкладку "отправленные"
    5 поиск последнего отправленного сообщения, считывание параметров в объект класса Message
    6 сравнение Message из вкладки "отправленные" с тестовыми данными, использовавшимися для составления письма

    :param app:  фикстура pytest
    :return:
    """
    address = message.address
    subject = message.subject
    body_message = message.body_message
    page = app.page_object
    with allure.step("Открытие и заполнение формы"):
        add_button = page.get_button_create_new_message()
        assert add_button, "Не найдена кнопка 'Написать'"
        add_button.click()
        address_field = page.get_field_address_destination()
        assert address_field, "Не найдено поле 'Получатели', либо не открылась форма 'Новое сообщение'"
        address_field.fill_text_field(address)
        subject_field = page.get_field_subject_during_create_message()
        assert subject_field, "Не найдено поле 'Тема', либо не открылась форма 'Новое сообщение'"
        subject_field.fill_text_field(subject)
        message_body_text_field = page.get_field_body_message_during_create_message()
        assert message_body_text_field, "Не найдено поле 'Тело письма', либо не открылась форма 'Новое сообщение'"
        message_body_text_field.fill_text_field(body_message)
    with allure.step("Отправка сообщения"):
        send_button = page.get_send_button()
        assert send_button, "Кнопка Отправить не найдена"
        send_button.click()
    with allure.step("Поиск последнего отправленного сообщения, считывание параметров в объект класса Message"):
        sent_pane_menu_item = page.open_pane_sent()
        assert sent_pane_menu_item, "Не найден раздел меню 'Отправленные', либо не найдена панель вкладок разделов"
        sent_pane_menu_item.click()
        page.open_first_message_from_sent_table()
        read_message = page.read_message_parameters()
    with allure.step("сравнение Message из вкладки 'отправленные' с тестовыми данными,\
     использовавшимися для составления письма"):
        assert read_message.address == address, f'Найденное значение{read_message.address} почтового адреса не \
        соответствует тестовому значению почтового адреса{address}'
        assert read_message.subject == subject, f'Найденное значение{read_message.address} темы сообщения не \
        соответствует тестовому значению темы {subject}'
        assert read_message.body_message == body_message, f'Найденное значение{read_message.body_message} тела сообщения\
         не соответствует тестовому значению {body_message}'







