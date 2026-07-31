import requests
import allure

from urls import Urls
from data import Messages
from api_methods import get_first_order_id


class TestAcceptOrder:

    @allure.title('Успешное принятие заказа возвращает код 200 и тело ok:true')
    def test_accept_order_valid_data_returns_200_and_ok_true(self, create_courier):
        order_id = get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id), params={"courierId": create_courier["id"]})

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Принятие заказа без id курьера возвращает ошибку 400')
    def test_accept_order_without_courier_id_returns_400(self):
        order_id = get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id))

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Принятие заказа с неверным id курьера возвращает ошибку 404')
    def test_accept_order_wrong_courier_id_returns_404(self):
        order_id = get_first_order_id()

        response = requests.put(Urls.ACCEPT_ORDER + str(order_id), params={"courierId": 0})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_COURIER_NOT_EXIST

    @allure.title('Принятие заказа без id заказа возвращает ошибку 404')
    def test_accept_order_without_order_id_returns_404(self, create_courier):
        response = requests.put(Urls.ACCEPT_ORDER, params={"courierId": create_courier["id"]})

        assert response.status_code == 404

    @allure.title('Принятие заказа с неверным id заказа возвращает ошибку 404')
    def test_accept_order_wrong_order_id_returns_404(self, create_courier):
        response = requests.put(Urls.ACCEPT_ORDER + "0", params={"courierId": create_courier["id"]})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_NOT_EXIST