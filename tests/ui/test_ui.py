import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    #create object for use browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    #open GitHub login page
    driver.get("https://github.com/login")

    #find field when enter the incorrect name
    login_elem = driver.find_element(By.ID, "login_field")

    #find field when enter the incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    #enter the incorrect name or email
    login_elem.send_keys("sergiibutenko@mistakeinimail.com")
    time.sleep(1)

    #enter the incorrect password
    pass_elem.send_keys("12345678")
    time.sleep(1)

    #find sing in button
    btn_elem = driver.find_element(By.NAME, "commit")

    #emulate click LMB
    btn_elem.click()
    time.sleep(1)

    #assert the title of login page
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(1)

    #close browser
    driver.close()


@pytest.mark.ui
def test_check_tracking_TTN():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Відкриваємо сторінку https://intime.check-track.com/ua/
    driver.get("https://intime.check-track.com/ua/")

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "≡ ІнТайм ᐈ Відстежити посилку, товар, вантаж"
    time.sleep(3)

    #Знаходимо поле вводу ТТН
    search_elem = driver.find_element(By.ID, "search")

    #Вводимо неправильний номер ТТН
    search_elem.send_keys("4556532255")

    #Знаходимо кнопку Пошук
    btn_elem = driver.find_element(By.CLASS_NAME, "btn-search.text-uppercase")

    #Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    #Закріваємо браузер
    driver.close()