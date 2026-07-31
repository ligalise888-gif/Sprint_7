import requests
import allure

from urls import Urls


class TestOrdersList:

    @allure.title('Получение списка заказов возвращает код 200 и непустой список orders')
    def test_get_orders_list_returns_200_and_orders_list(self):
        response = requests.get(Urls.GET_ORDERS_LIST)

        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
        assert len(response.json()["orders"]) > 0