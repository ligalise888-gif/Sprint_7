import pytest
import requests

from urls import Urls
from data import OrderData
from api_methods import register_new_courier_and_return_login_password, get_courier_id


@pytest.fixture
def create_courier():
    # создаёт нового курьера перед тестом, после теста удаляет его
    courier = register_new_courier_and_return_login_password()
    courier_id = get_courier_id(courier["login"], courier["password"])
    courier["id"] = courier_id

    yield courier

    requests.delete(Urls.DELETE_COURIER + str(courier_id))


@pytest.fixture
def delete_courier_after_test():
    # тест сам создаёт курьера и кладёт login/password в этот словарь,
    # фикстура удаляет курьера после теста
    courier = {}

    yield courier

    if courier.get("login") and courier.get("password"):
        courier_id = get_courier_id(courier["login"], courier["password"])
        if courier_id is not None:
            requests.delete(Urls.DELETE_COURIER + str(courier_id))


@pytest.fixture
def create_order_and_return_track():
    # создаёт заказ и возвращает его track
    payload = OrderData.ORDER_BODY.copy()
    payload["color"] = ["BLACK"]
    response = requests.post(Urls.CREATE_ORDER, json=payload)
    track = response.json()["track"]

    yield track

    # отмена заказа после теста (track передаётся в params)
    requests.put(Urls.BASE_URL + '/api/v1/orders/cancel', params={"track": track})