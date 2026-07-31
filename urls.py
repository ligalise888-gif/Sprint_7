class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER = BASE_URL + '/api/v1/courier'
    LOGIN_COURIER = BASE_URL + '/api/v1/courier/login'
    DELETE_COURIER = BASE_URL + '/api/v1/courier/'          # + id
    CREATE_ORDER = BASE_URL + '/api/v1/orders'
    GET_ORDERS_LIST = BASE_URL + '/api/v1/orders'
    ACCEPT_ORDER = BASE_URL + '/api/v1/orders/accept/'      # + id
    GET_ORDER_BY_TRACK = BASE_URL + '/api/v1/orders/track'