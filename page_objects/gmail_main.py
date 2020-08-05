# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from fw.common_web_elements import TextField, Button, PermanentField
from model.messsage import Message
from selenium.webdriver.common.action_chains import ActionChains


button_add_new_message = (By.XPATH, "//div[@role='button' and (contains(text(),'аписать'))]")
addressee_destination_field = (By.XPATH, "//div[@role='region']//textarea[@aria-label='Кому']")
subject_field = (By.XPATH, "//div[@role='region']//input[@name='subjectbox']")
new_message_field = {"pre_action": (By.XPATH, "//div[@role='region']//table[@id='undefined']//td[2]"),
                     "main_text_field": (By.XPATH, "//div[@role='region']//table[@id='undefined']//div[@aria-multiline]")}
send_button = (By.XPATH, "//div[@role='region']//div[@role='button' and @aria-label and text()]")
button_to_open_sent_pane = (By.XPATH, "//span/a[contains(@href,'sent')]")

first_message_in_sent_table = (By.XPATH, "//div[@role='main']//table[@aria-readonly='true']/tbody/tr[1]/td[5]")
MESSAGE_CARD = {
    'addresser': (By.XPATH, "//div[@role='listitem']//tbody/tr[2]//span[@dir]"),
    'subject': (By.XPATH, "//h2[@data-thread-perm-id]"),
    'message_body': (By.XPATH, "//div[@data-message-id]//div[text()]")
                }

class MainPage:
    def __init__(self, app):
        self.wrapper = app
        if not self.wrapper.is_logged_in():
            self.wrapper.crooked_login(username="golom3402service", password="$ervic360l0m34o2")



    def get_button_create_new_message(self):
        button = Button(self.wrapper, button_add_new_message)
        return button if button else None


    def get_field_address_destination(self):
        field = TextField(self.wrapper, addressee_destination_field)
        return field if field else None

    def get_field_subject_during_create_message(self):
        field = TextField(self.wrapper, subject_field)
        return field if field else None

    def get_field_body_message_during_create_message(self):
        pre_field = self.wrapper.get_element_by_locator(new_message_field['pre_action'])
        pre_field.click()
        self.wrapper.wait_to_be_clickable(new_message_field['main_text_field'])
        field = TextField(self.wrapper, new_message_field['main_text_field'])
        return field if field else None

    def get_send_button(self):
        button = Button(self.wrapper, send_button)
        return button if button else None

    def open_pane_sent(self):
        """
        Метод возвращает web-element пункта меню, для переключения на вкладку "Отправленные"
        :return: web_element
        """
        button = Button(self.wrapper, button_to_open_sent_pane)
        return button if button else None

    def open_first_message_from_sent_table(self):
        self.wrapper.wait_to_be_clickable(first_message_in_sent_table)
        element = self.wrapper.get_element_by_locator(first_message_in_sent_table)
        hover = ActionChains(self.wrapper.wd).move_to_element(element)
        hover.perform()
        element.click()
        self.wrapper.wait_to_end_all_query()


    def read_message_parameters(self):
        """
        Метод считывает аттрибуты сообщения из раскрытой карточки сообщения
        :return:
        """
        address = self.wrapper.get_element_by_locator(MESSAGE_CARD['addresser']).get_attribute("email")

        subject_field = PermanentField(self.wrapper, MESSAGE_CARD['subject'])
        subject_text = subject_field.get_text()
        subject = '' if subject_text == "(без темы)" else subject_text
        message = ''
        for i in self.wrapper.wd.find_elements(*MESSAGE_CARD['message_body']):
            message += i.text
        return Message(address=address, subject=subject, body_message=message)


