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

    COURIER = f"{MAIN_URL}/api/v1/courier"
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
    ORDERS_TEST_DATA = [
          {
              "firstName": "Max",
              "lastName": "Ivanov",
              "address": "Ivanovo, 2",
              "metroStation": 2,
              "phone": "+7 800 355 35 35",
              "rentTime": 2,
              "deliveryDate": "2020-06-07",
              "comment": "Please call me",
              "color": ["BLACK"]
          },
          {
              "firstName": "Ivan",
              "lastName": "Ivanov",
              "address": "Anyova, 3",
              "metroStation": 4,
              "phone": "+7 800 355 15 32",
              "rentTime": 6,
              "deliveryDate": "'2020-06-06",
              "comment": "Please call me",
              "color": ["GREY"]
          },
          {
              "firstName": "Anya",
              "lastName": "Anyova",
              "address": "Svetovo, 5",
              "metroStation": 1,
              "phone": "+7 800 355 35 35",
              "rentTime": 4,
              "deliveryDate": "'2020-06-10",
              "comment": "Please call me",
              "color": ["GREY"]
          },
          {
              "firstName": "Gogi",
              "lastName": "Gogiani",
              "address": "Maxovo, 1",
              "metroStation": 3,
              "phone": "+7 670 355 35 25",
              "rentTime": 2,
              "deliveryDate": "'2020-06-09",
              "comment": "Please call me",
              "color": ["BLACK", "GREY"]
          },
          {
              "firstName": "Sveta",
              "lastName": "Svetikova",
              "address": "Marta, 6",
              "metroStation": 6,
              "phone": "+7 800 355 34 34",
              "rentTime": 1,
              "deliveryDate": "'2020-06-08",
              "comment": "Please call me"
          },
          {
              "firstName": "Marina",
              "lastName": "Marinomax",
              "address": "Gogiani, 4",
              "metroStation": 4,
              "phone": "+7 800 355 35 35",
              "rentTime": 5,
              "deliveryDate": "'2020-06-08",
              "comment": "Please call me"
          }
    ]