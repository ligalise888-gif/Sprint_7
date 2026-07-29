import requests
import allure

from urls import Urls
from data import CourierData, Messages
from helpers import generate_random_string, register_new_courier_and_return_login_password, get_courier_id


class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными возвращает код 201 и тело ok:true')
    def test_create_courier_valid_data_returns_201_and_ok_true(self):
        login = generate_random_string(10)
        payload = {"login": login, "password": CourierData.PASSWORD, "firstName": CourierData.FIRST_NAME}

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        courier_id = get_courier_id(login, CourierData.PASSWORD)
        if courier_id is not None:
            requests.delete(Urls.DELETE_COURIER + str(courier_id))

    @allure.title('Нельзя создать двух курьеров с одинаковым логином')
    def test_create_two_identical_couriers_returns_409(self):
        login_pass = register_new_courier_and_return_login_password()
        login, password, first_name = login_pass[0], login_pass[1], login_pass[2]

        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.LOGIN_ALREADY_USED

        courier_id = get_courier_id(login, password)
        if courier_id is not None:
            requests.delete(Urls.DELETE_COURIER + str(courier_id))

    @allure.title('Создание курьера без обязательного поля возвращает ошибку 400')
    def test_create_courier_without_required_field_returns_400(self):
        payload_no_login = {"password": CourierData.PASSWORD, "firstName": CourierData.FIRST_NAME}
        response_no_login = requests.post(Urls.CREATE_COURIER, data=payload_no_login)
        assert response_no_login.status_code == 400
        assert response_no_login.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_CREATE

        payload_no_password = {"login": generate_random_string(10), "firstName": CourierData.FIRST_NAME}
        response_no_password = requests.post(Urls.CREATE_COURIER, data=payload_no_password)
        assert response_no_password.status_code == 400
        assert response_no_password.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_CREATE