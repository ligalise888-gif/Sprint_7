import requests
import allure

from urls import Urls
from data import Messages


class TestDeleteCourier:

    @allure.title('Успешное удаление курьера возвращает код 200 и тело ok:true')
    def test_delete_courier_valid_id_returns_200_and_ok_true(self, create_courier):
        response = requests.delete(Urls.DELETE_COURIER + str(create_courier["id"]))

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без id возвращает ошибку 404')
    def test_delete_courier_without_id_returns_404(self):
        response = requests.delete(Urls.DELETE_COURIER)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.DELETE_NOT_FOUND

    @allure.title('Удаление курьера с несуществующим id возвращает ошибку 404')
    def test_delete_courier_nonexistent_id_returns_404(self):
        response = requests.delete(Urls.DELETE_COURIER + "0")

        assert response.status_code == 404
        assert response.json()["message"] == Messages.COURIER_NOT_FOUND