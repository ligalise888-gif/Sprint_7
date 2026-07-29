import requests
import allure

from urls import Urls
from data import Messages
from helpers import register_new_courier_and_return_login_password, get_courier_id


class TestAcceptOrder:

    def _get_first_order_id(self):
        # берём id первого доступного заказа из общего списка
        response = requests.get(Urls.GET_ORDERS_LIST)
        return response.json()["orders"][0]["id"]

    @allure.title('Успешное принятие заказа возвращает код 200 и тело ok:true')
    def test_accept_order_valid_data_returns_200_and_ok_true(self):
        login_pass = register_new_courier_and_return_login_password()
        courier_id = get_courier_id(login_pass[0], login_pass[1])
        order_id = self._get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id), params={"courierId": courier_id})

        assert response.status_code == 200
        assert response.json() == {"ok": True}

        requests.delete(Urls.DELETE_COURIER + str(courier_id))

    @allure.title('Принятие заказа без id курьера возвращает ошибку 400')
    def test_accept_order_without_courier_id_returns_400(self):
        order_id = self._get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id))

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Принятие заказа с неверным id курьера возвращает ошибку 404')
    def test_accept_order_wrong_courier_id_returns_404(self):
        order_id = self._get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id), params={"courierId": 0})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_COURIER_NOT_EXIST

    @allure.title('Принятие заказа без id заказа возвращает ошибку 404')
    def test_accept_order_without_order_id_returns_404(self):
        login_pass = register_new_courier_and_return_login_password()
        courier_id = get_courier_id(login_pass[0], login_pass[1])

        response = requests.put(Urls.ACCEPT_ORDER, params={"courierId": courier_id})

        assert response.status_code == 404

        requests.delete(Urls.DELETE_COURIER + str(courier_id))

    @allure.title('Принятие заказа с неверным id заказа возвращает ошибку 404')
    def test_accept_order_wrong_order_id_returns_404(self):
        login_pass = register_new_courier_and_return_login_password()
        courier_id = get_courier_id(login_pass[0], login_pass[1])

        response = requests.put(Urls.ACCEPT_ORDER + "0", params={"courierId": courier_id})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_NOT_EXIST

        requests.delete(Urls.DELETE_COURIER + str(courier_id))