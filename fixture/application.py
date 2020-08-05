# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from page_objects.gmail_main import MainPage
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://mail.google.com/mail"


default_await = 10

SINGLE_TONE = None


crooked_url_start = "http://stackoverflow.com/users/login"
crooked_button_to_google = (By.XPATH, "//button[@data-provider='google']")
button_to_sign_out_widget = (By.XPATH, "//a[@role='button' and (contains(@href,'SignOut'))]")
button_to_log_out = (By.XPATH, "//a[contains(@href,'Logout')]")

username_field = (By.XPATH, "//input[@type='email']")
login_next_button = (By.XPATH, "//div[@data-is-touch-wrapper='true']//button[@type='button']")
password_field = (By.XPATH, "//form[contains(@action,'password')]//input[@type='password']")


class Application:
    def __init__(self, browser='firefox'):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        self.wd.set_window_size(1920, 1080)
        self.page_object = MainPage(self)


    def crooked_login(self, username, password):
        wd = self.wd
        wd.get(crooked_url_start)
        self.get_element_by_locator(crooked_button_to_google).click()
        self.wait_to_end_all_query()
        sleep(5)
        if not self.is_element_present(username_field):
            pass
        user_field = self.get_element_by_locator(username_field)
        user_field.send_keys(username)
        self.get_element_by_locator(login_next_button).click()
        sleep(5)
        self.wait_to_end_all_query()
        self.wait_to_be_clickable(password_field)
        pass_field = self.get_element_by_locator(password_field)
        pass_field.send_keys(password)
        self.get_element_by_locator(login_next_button).click()
        wd.get(base_url)
        sleep(5)

    def logout(self):
        wd = self.wd
        button_sign_out = self.get_element_by_locator(button_to_sign_out_widget)
        button_sign_out.click()
        button_log_out = self.get_element_by_locator(button_to_log_out)
        button_log_out.click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def is_logged_in(self):
        wd = self.wd
        a = self.get_element_by_locator(button_to_sign_out_widget)
        if a:
            return True
        else:
            return False

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def destroy(self):
        self.wd.quit()

    def get_element_by_locator(self, locator):
        """
        Реализует поиск элемента по локатору
        :param locator: локатор
        :return:
        """
        try:
            return self.wd.find_element(*locator)
        except NoSuchElementException:
            #logger.info('Не удалось найти по {} элемент {}'.format(*locator))
            return None

    def wait_element(self, element, await_time=None):
        """
        Ожидание загрузки элемента
        :param element: - локатор элемента в формате (By.***, "locator").
        :param await_time:
        :return:
        """

        result = True
        try:
            WebDriverWait(self.wd, await_time if await_time else default_await
                          ).until((EC.visibility_of_element_located(*element)))
        except TimeoutException:
            #logger.info('Не дождались появления элемента "{}" через {} секунд'.format(elem, await_time))
            result = False
        return result

    def wait_to_be_clickable(self, element):
        """
        Ожидание того, что элемент станет "кликабельным"
        :param element: - локатор элемента в формате (By.***, "locator").
        """
        result=True
        try:
            element=WebDriverWait(self.wd, 10).until(EC.element_to_be_clickable(element))
        except TimeoutException:
            #logger.info(f'Элемент {element[1]} не становится кликабельным за 10сек')
            result = False
        return result

    def is_element_present(self, element):
        """
        Метод ищет элемент в дереве DOM и возвращает True или None в зависимости от результата
        :param element: - локатор элемента в формате (By.***, "locator").
        """
        try:
            element = self.wd.find_element(*element)
            return True
        except NoSuchElementException:
            return None


    def wait_to_end_all_query(self, await_time=None):
        result = True
        wait = WebDriverWait(self.wd, await_time if await_time else default_await)
        try:
            wait.until(lambda driver: self.wd.execute_script('return document.readyState') == 'complete')
        except TimeoutException:
            # logger.info('Не дождались состояния готовности браузера после выполнения всех\
            #       запросов через {} секунд'.format(await_time))
            result = False
        return result


    def __del__(self):
        self.wd.quit()


def get_driver():
    global SINGLE_TONE
    if SINGLE_TONE is not None:
        return SINGLE_TONE
    else:
        SINGLE_TONE = Application(browser='firefox')
        SINGLE_TONE.wd.get(base_url)
        return SINGLE_TONE