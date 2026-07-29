import requests
import allure

from urls import Urls
from data import OrderData, Messages


class TestGetOrderByTrack:

    @allure.title('Получение заказа по валидному track возвращает код 200 и объект заказа')
    def test_get_order_by_valid_track_returns_200_and_order(self, create_order_and_return_track):
        track = create_order_and_return_track

        response = requests.get(Urls.GET_ORDER_BY_TRACK, params={"t": track})

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title('Получение заказа без номера возвращает ошибку 400')
    def test_get_order_without_track_returns_400(self):
        response = requests.get(Urls.GET_ORDER_BY_TRACK)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Получение заказа с несуществующим номером возвращает ошибку 404')
    def test_get_order_by_nonexistent_track_returns_404(self):
        response = requests.get(Urls.GET_ORDER_BY_TRACK, params={"t": 0})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ORDER_NOT_FOUND