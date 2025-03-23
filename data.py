import json


class StatusCode:
    OK_200 = 200
    CREATED_201 = 201
    NOT_FOUND_404 = 404
    BAD_REQUEST_400 = 400
    CONFLICT_409 = 409
    INTERNAL_SERVER_ERROR_500 = 500
    GATEWAY_TIMEOUT_504 = 504


class Api:
    MAIN_URL = "https://qa-scooter.praktikum-services.ru"

    CREATE_COURIER = f"{MAIN_URL}/api/v1/courier"
    COURIER_LOGIN = f"{MAIN_URL}/api/v1/courier/login"
    ORDERS = f"{MAIN_URL}/api/v1/orders"
    ORDERS_LIST = f"{MAIN_URL}/api/v1/orders"


class ResponseMessage:
    CREATED_RESPONSE = {'ok': True}
    REQUIRED_FIELDS_NOT_FOUND = "Недостаточно данных для создания учетной записи"
    REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN = "Недостаточно данных для входа"
    LOGIN_EXISTS = "Этот логин уже используется. Попробуйте другой."
    USER_NOT_FOUND = "Учетная запись не найдена"

class Data:
    COURIER_IDS = [1, 2, 3, 4, 5]

    ORDER_PAGE_PARAMS = [
        {"limit": 1, "page": 0},
        {"limit": 5, "page": 2},
        {"limit": 10, "page": 3},
        {"limit": 15, "page": 4},
    ]

    @staticmethod
    def order_data():
        """
        Используются данные, которые я перемешала в https://pairwise.teremokgames.com/
        """
        order_data = None
        with open("order_test_data.json", "r") as json_file:
            order_data = json.load(json_file)

        return order_data

