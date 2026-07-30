import requests
import allure

from urls import Urls
from data import CourierData, Messages
from helpers import generate_random_string


class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными возвращает код 201 и тело ok:true')
    def test_create_courier_valid_data_returns_201_and_ok_true(self, delete_courier_after_test):
        login = generate_random_string(10)
        payload = {"login": login, "password": CourierData.PASSWORD, "firstName": CourierData.FIRST_NAME}

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # передаём данные в фикстуру для удаления
        delete_courier_after_test["login"] = login
        delete_courier_after_test["password"] = CourierData.PASSWORD

    @allure.title('Нельзя создать двух курьеров с одинаковым логином')
    def test_create_two_identical_couriers_returns_409(self, create_courier):
        payload = {
            "login": create_courier["login"],
            "password": create_courier["password"],
            "firstName": create_courier["firstName"]
        }
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.LOGIN_ALREADY_USED

    @allure.title('Создание курьера без обязательного поля login возвращает ошибку 400')
    def test_create_courier_without_login_returns_400(self):
        payload = {"password": CourierData.PASSWORD, "firstName": CourierData.FIRST_NAME}
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_CREATE

    @allure.title('Создание курьера без обязательного поля password возвращает ошибку 400')
    def test_create_courier_without_password_returns_400(self):
        payload = {"login": generate_random_string(10), "firstName": CourierData.FIRST_NAME}
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_CREATE