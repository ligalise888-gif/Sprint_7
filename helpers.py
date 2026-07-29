import requests
import random
import string

from urls import Urls


def generate_random_string(length):
    # генерирует строку из букв нижнего регистра заданной длины
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password():
    # регистрирует нового курьера и возвращает список [login, password, first_name]
    # если регистрация не удалась, возвращает пустой список
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATE_COURIER, data=payload)

    login_pass = []
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def get_courier_id(login, password):
    # авторизует курьера и возвращает его id
    payload = {"login": login, "password": password}
    response = requests.post(Urls.LOGIN_COURIER, data=payload)
    return response.json().get("id")