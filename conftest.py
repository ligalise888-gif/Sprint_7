import pytest
import requests

from urls import Urls
from data import OrderData
from helpers import register_new_courier_and_return_login_password, get_courier_id


@pytest.fixture
def create_courier():
    # создаёт нового курьера перед тестом, после теста удаляет его
    login_pass = register_new_courier_and_return_login_password()
    login = login_pass[0]
    password = login_pass[1]
    first_name = login_pass[2]

    yield {"login": login, "password": password, "firstName": first_name}

    # удаление курьера после теста
    courier_id = get_courier_id(login, password)
    if courier_id is not None:
        requests.delete(Urls.DELETE_COURIER + str(courier_id))


@pytest.fixture
def create_order_and_return_track():
    # создаёт заказ и возвращает его track для тестов accept / get by track
    payload = OrderData.ORDER_BODY.copy()
    payload["color"] = ["BLACK"]
    response = requests.post(Urls.CREATE_ORDER, json=payload)
    track = response.json().get("track")

    yield track

    # отмена заказа после теста (track передаётся в params, id в теле по доке)
    requests.put(Urls.BASE_URL + '/api/v1/orders/cancel', params={"track": track})