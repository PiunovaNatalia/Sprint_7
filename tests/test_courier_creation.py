import allure
import requests

from data import ResponseMessage, StatusCode, Api


class TestCourierCreation:
    @allure.title('Тестирование успешного создания курьера')
    @allure.description(
        "Генерируем случайные логин, пароль и имя курьера. "
        "Создаем пейлоад и передаем на ручку создания курьера эти параметры, "
        "в ответ поулчаем успешный статус код 201"
    )
    def test_courier_successful_creation(self, generate_random_courier_data):
        login, password, first_name = generate_random_courier_data

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Api.COURIER, data=payload)

        assert (response.status_code == StatusCode.CREATED_201
                and response.json() == ResponseMessage.CREATED_RESPONSE)

    @allure.title('Тестирование попытки создать двух одинаковых курьеров')
    @allure.description(
        "Генерируем случайные логин, пароль и имя курьера. "
        "Создаем пейлоад и передаем на ручку создания курьера эти параметры, "
        "в ответ поулчаем успешный статус код 201,"
        "далее с этими же данными пытаемся сделать еще один запрос,"
        "в результате получаем статус код 409"
    )
    def test_courier_creation_with_same_login(self, generate_random_courier_data):
        login, password, first_name = generate_random_courier_data

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response_first_courier = requests.post(Api.COURIER, data=payload)
        response_second_courier = requests.post(Api.COURIER, data=payload)

        assert (response_second_courier.status_code == StatusCode.CONFLICT_409
                and response_second_courier.json()["message"]  == ResponseMessage.LOGIN_EXISTS)

    @allure.title('Тестирование создания курьера без переданного лоигна')
    @allure.description(
        "Генерируем случайные пароль и имя курьера. "
        "Создаем пейлоад и передаем на ручку создания курьера эти параметры, "
        "в ответ поулчаем успешный статус код 400"
    )
    def test_courier_creation_without_login(self, generate_random_courier_data):
        _, password, first_name = generate_random_courier_data

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Api.COURIER, data=payload)

        assert (response.status_code == StatusCode.BAD_REQUEST_400
                and response.json()["message"]  == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND)

    @allure.title('Тестирование создания курьера без переданного пароля')
    @allure.description(
        "Генерируем случайные логин и имя курьера. "
        "Создаем пейлоад и передаем на ручку создания курьера эти параметры, "
        "в ответ поулчаем успешный статус код 400"
    )
    def test_courier_creation_without_password(self, generate_random_courier_data):
        login, _, first_name = generate_random_courier_data

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(Api.COURIER, data=payload)

        assert (response.status_code == StatusCode.BAD_REQUEST_400
                and response.json()["message"]  == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND)

    @allure.title('Тестирование создания курьера с уже существующим логином')
    @allure.description(
        "Генерируем случайные логин, пароль имя курьера. "
        "Создаем пейлоад и передаем на ручку создания курьера эти параметры, "
        "в ответ поулчаем успешный статус код 400 - так создан первый курьер. "
        "Далее с ранее созданным логином и новыми паролем и менем пытаемся создать нового курьера, "
        "в результате получаем статус код 409."
    )
    def test_courier_creation_login_already_exist(self, generate_random_courier_data):
        one_login, password, first_name = generate_random_courier_data

        payload = {
            "login": one_login,
            "password": password,
            "firstName": first_name
        }

        response_first_courier = requests.post(Api.COURIER, data=payload)

        _, password, first_name = generate_random_courier_data

        payload = {
            "login": one_login,
            "password": password,
            "firstName": first_name
        }

        response_second_courier = requests.post(Api.COURIER, data=payload)

        assert (response_second_courier.status_code == StatusCode.CONFLICT_409
                and response_second_courier.json()["message"]  == ResponseMessage.LOGIN_EXISTS)
