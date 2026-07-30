import requests
import random
import string

import allure

from urls import Urls


@allure.step('Сгенерировать случайную строку заданной длины')
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step('Зарегистрировать нового курьера и вернуть его данные')
def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    requests.post(Urls.CREATE_COURIER, data=payload)

    return {"login": login, "password": password, "firstName": first_name}


@allure.step('Авторизовать курьера и получить его id')
def get_courier_id(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(Urls.LOGIN_COURIER, data=payload)
    return response.json().get("id")


@allure.step('Получить id первого доступного заказа из списка')
def get_first_order_id():
    response = requests.get(Urls.GET_ORDERS_LIST)
    return response.json()["orders"][0]["id"]