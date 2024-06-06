from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import TrackingTTN
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #Створеня об'єкту сторінки
    sign_in_page = SignInPage()

    #відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    #викоуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title ("Sign in to GitHub \xb7 GitHub")

    #Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_check_inc_TTN_page_object():
    #Створеня об'єкту сторінки
    tracking_ttn = TrackingTTN()

    #відкриваємо сторінку
    tracking_ttn.go_to()

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert tracking_ttn.check_title ("≡ ІнТайм ᐈ Відстежити посилку, товар, вантаж")

    #виконуємо спробу пошуку ттн
    tracking_ttn.try_search("4556532255")

    #Закриваємо браузер
    tracking_ttn.close()