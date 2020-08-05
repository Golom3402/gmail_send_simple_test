from time import sleep

from selenium.webdriver.common.by import By

username = 'golom3402service@gmail.com'
password = "C0pperm@ngoogle"
password = "$ervic360l0m34o2"



base_url = "https://mail.google.com"
crooked_url_start = "http://stackoverflow.com/users/login"
crooked_button_to_google = "//button[@data-provider='google']"


username_field = (By.XPATH,"//input[@type='email']")
login_next_button = (By.XPATH,"//div[@data-is-touch-wrapper='true']//button[@type='button']")
password_field = (By.XPATH,"//form[contains(@action,'password')]//input[@type='password']")




button_add_new_message = (By.XPATH,"//div[@role='button' and (contains(text(),'аписать'))]")




button_to_login_from_about_page = ""

"//div[@class='h-c-header__cta h-c-header__cta--tier-two']//a[@ga-event-action='sign in' and contains(@href,'AccountChooser')]"


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def crooked_login(self, username, password):
        wd = self.app.wd
        wd.get(crooked_url_start)
        wd.find_element(crooked_button_to_google).click()
        self.app.wait_to_end_all_query()
        sleep(5)
        if not self.app.is_element_present(username_field):
            pass
        user_field = wd.find_element(username_field)
        user_field.send_keys(username)
        wd.find_element(login_next_button).click()
        sleep(5)
        self.app.wait_to_end_all_query()
        self.app.wait_to_be_clickable(password_field)
        pass_field = wd.find_element(password_field)
        pass_field.send_keys(password)
        wd.find_element(login_next_button)
        sleep(5)











    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, name, password):
        if self.is_logged_in():
            if self.is_logged_in_as(name):
                return
            else:
                self.logout()
        self.login(name, password)


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        logged = self.get_logged_user()
        return logged == username

    def get_logged_user(self):
        wd = self.app.wd
        text = wd.find_element_by_xpath("//form[@name='logout']/b").text[1:-1]
        return text





https://accounts.google.com/signin/oauth/consent?authuser=0&part=AJi8hANe2eBxEZWsmVj0LBV8UaAqsjOYg2EPY2gcpFI8Sf7G-9-oyYeewMVly5zeTAlUtdhAs5caofCQ_wDijljVajE4y7E3ohMFAjxeWmSkZDCMmbBX5rnvgI-yCf2O97J7tGgREy2_HYgsWTPgTEPgoc9qPnhTXazxWGUWgKS0WHaOKdOR_n-iPr08lncCoh0dsvTqbr2WZjb6PeDbGE57G3MqMEPxD1S2N2KOC8xobPLniqavMWHEPwasD_eKX36_yy_GJt3H9aOPVJ9SyHdC04t_K8LuUIbILBlz_S4hEXcu8fYuyhUro9PYaB3OP-wsHv8lFeVfLM6NlHRKTXBpABQkqAl_fx_3WR6G5AH0yis7gZMxdnThCYT7wqgrO5nfYXKJ2VsjdumSRsTfze8RFuOdJ59y_28rAwjVOgnPQz5tHC6KHXAKW9e3m73kVvf3V-mhSZd_&as=S-1811622228%3A1596482376362490&pli=1&rapt=AEjHL4OV8iS_F09w9S8ZsDiESlr0sYotjxNl_RlcE2i4lnxsaBZtOg6Njct3fio6QhDIsfrZ2KDDwt5knlbeYELnfyvYyacmtw
