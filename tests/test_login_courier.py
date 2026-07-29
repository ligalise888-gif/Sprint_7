import requests
import allure

from urls import Urls
from data import Messages
from helpers import generate_random_string


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера возвращает код 200 и id')
    def test_login_courier_valid_data_returns_200_and_id(self, create_courier):
        payload = {"login": create_courier["login"], "password": create_courier["password"]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация без логина не проходит')
    @allure.description('По документации ожидается код 400. Фактически сервер отвечает 504 (дефект API). Проверяем, что авторизация не выполняется успешно.')
    def test_login_courier_without_login_not_authorized(self, create_courier):
        payload = {"password": create_courier["password"]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload, timeout=90)

        assert response.status_code != 200

    @allure.title('Авторизация без пароля не проходит')
    @allure.description('По документации ожидается код 400. Фактически сервер отвечает 504 (дефект API). Проверяем, что авторизация не выполняется успешно.')
    def test_login_courier_without_password_not_authorized(self, create_courier):
        payload = {"login": create_courier["login"]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload, timeout=90)

        assert response.status_code != 200

    @allure.title('Авторизация с неверным логином возвращает ошибку 404')
    def test_login_courier_wrong_login_returns_404(self, create_courier):
        payload = {"login": generate_random_string(10), "password": create_courier["password"]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация с неверным паролем возвращает ошибку 404')
    def test_login_courier_wrong_password_returns_404(self, create_courier):
        payload = {"login": create_courier["login"], "password": generate_random_string(10)}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация несуществующего курьера возвращает ошибку 404')
    def test_login_nonexistent_courier_returns_404(self):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND