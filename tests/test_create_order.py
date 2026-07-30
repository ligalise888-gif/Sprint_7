import requests
import allure
import pytest

from urls import Urls
from data import OrderData


class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета возвращает код 201 и track')
    @allure.description('Проверяем цвета: BLACK, GREY, оба, без цвета')
    @pytest.mark.parametrize('color', OrderData.COLORS)
    def test_create_order_with_different_colors_returns_track(self, color):
        payload = OrderData.ORDER_BODY.copy()
        payload["color"] = color

        response = requests.post(Urls.CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()