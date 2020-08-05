# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
#logger = logger_handler.get_logger('common_web_element')
from time import sleep

class TextField():
    def __init__(self, wdwrapper, locator):
        self.wdwrapper = wdwrapper
        self.wd_element = wdwrapper.get_element_by_locator(locator)
        #if self.wd_element is None:
        #logger.debug('Не найдено поле ввода')



    def clear_text_field(self, backspace=False):
        # logger.debug('Очистим строку ввода')
        self.wd_element.clear()
        if backspace:
            self.wd_element.send_keys('F', Keys.BACK_SPACE)

    def fill_text_field(self, text=''):
        #logger.debug('Заполнеяем поле ввода текстом: "{}"'.format(text))
        if self.get_current_values() != '':
            self.clear_text_field()
        self.wd_element.send_keys(text)
        self.wdwrapper.wait_to_end_all_query()

    def get_current_values(self):
        """
        Метод возвращает значение из атрибута value в строке ввода
        """
        #logger.debug('Получим текущее значение в строке ввода')
        return self.wd_element.get_attribute('value')

class Button():
    def __init__(self, wdwrapper, button_locator_dict):
        self.wdwrapper = wdwrapper
        self.locator = button_locator_dict
        self.wd_element = wdwrapper.get_element_by_locator(button_locator_dict)
        #if self.wd_element is None:
            #logger.debug('Не найдена кнопка')

    def click(self):
        self.wdwrapper.wait_to_be_clickable(self.locator)
        self.wd_element.click()
        self.wdwrapper.wait_to_end_all_query()

class PermanentField():
    def __init__(self, wdwrapper, locator):
        self.wdwrapper = wdwrapper
        self.locator = locator
        self.wd_element = wdwrapper.get_element_by_locator(locator)

    def get_text(self):
        return self.wd_element.text

