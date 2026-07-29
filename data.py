class CourierData:
    # валидные данные для создания курьера (логин генерируется в helpers)
    PASSWORD = "1234"
    FIRST_NAME = "saske"

    # наборы для проверки создания без обязательного поля
    WITHOUT_LOGIN = {"password": "1234", "firstName": "saske"}
    WITHOUT_PASSWORD = {"login": "ninja_no_pass", "firstName": "saske"}


class OrderData:
    # базовое тело заказа без цвета
    ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    # наборы цветов для параметризации создания заказа
    COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]


class Messages:
    # реальные сообщения об ошибках (сверено вручную в Postman)
    NOT_ENOUGH_DATA_TO_CREATE = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA_TO_LOGIN = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    ORDER_NOT_FOUND = "Заказ не найден"
    NOT_ENOUGH_DATA_TO_SEARCH = "Недостаточно данных для поиска"
    DELETE_NOT_FOUND = "Not Found."
    COURIER_NOT_FOUND = "Курьера с таким id нет."
    ACCEPT_COURIER_NOT_EXIST = "Курьера с таким id не существует"
    ACCEPT_ORDER_NOT_EXIST = "Заказа с таким id не существует"