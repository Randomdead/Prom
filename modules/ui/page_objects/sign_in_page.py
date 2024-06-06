from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #Знаходимо поле в яке будемо вводити неправильне ім'я користувача або поштову адрксу
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Вводимо неправильне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        #Знаходимо полк, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        #Вводимо неправильний пароль
        pass_elem.send_keys(password)

        #Знаходимо кнопку sing in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        #Емулюемо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    

class TrackingTTN(BasePage):
    URL = 'https://intime.check-track.com/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(TrackingTTN.URL)

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def try_search(self, ttn):
        #Знаходимо поле вводу ТТН
        search_elem = self.driver.find_element(By.ID, "search")

        #Вводимо неправильний номер ТТН
        search_elem.send_keys(ttn)

        #Знаходимо кнопку Пошук
        btn_elem = self.driver.find_element(By.CLASS_NAME, "btn-search.text-uppercase")

        #Емулюємо клік лівою кнопкою мишки
        btn_elem.click()