import allure
import requests

from data import ResponseMessage, StatusCode, Api


class TestCourierLogin:
    @allure.title('Тестирование авторизации курьера')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться"
    )
    def test_courier_authorisation(self, register_new_courier_and_return_login_password, delete_courier_by_id):
        login, password, _, courier_id = register_new_courier_and_return_login_password

        payload = {"login": login, "password": password}
        response = requests.post(Api.COURIER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.OK_200
            and isinstance(response.json()["id"], int)
        )

        delete_courier_by_id(courier_id)

    @allure.title('Тестирование авторизации курьера без пароля')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться без пароля"
    )
    def test_courier_authorisation_without_password(self, register_new_courier_and_return_login_password, delete_courier_by_id):
        login, _, _, courier_id = register_new_courier_and_return_login_password

        payload = {"login": login, "password": ""}
        response = requests.post(Api.COURIER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.BAD_REQUEST_400
            and response.json()["message"] == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN
        )
        delete_courier_by_id(courier_id)

    @allure.title('Тестирование авторизации курьера без логина')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться без логина"
    )
    def test_courier_authorisation_without_login(self, register_new_courier_and_return_login_password, delete_courier_by_id):
        _, password, _, courier_id = register_new_courier_and_return_login_password

        payload = {"login": "", "password": password}
        response = requests.post(Api.COURIER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.BAD_REQUEST_400
            and response.json()["message"] == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN
        )
        delete_courier_by_id(courier_id)

    @allure.title('Тестирование авторизации курьера с несуществующим логином')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться с несуществующим логином"
    )
    def test_courier_authorisation_with_wrong_login(self, register_new_courier_and_return_login_password, delete_courier_by_id):
        login, password, _, courier_id = register_new_courier_and_return_login_password

        payload = {"login": login + "_WRONG_LOGIN", "password": password}
        response = requests.post(Api.COURIER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.NOT_FOUND_404
            and response.json()["message"] == ResponseMessage.USER_NOT_FOUND
        )
        delete_courier_by_id(courier_id)

    @allure.title('Тестирование авторизации курьера с неправильным паролем')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться с неправильным паролем"
    )
    def test_courier_authorisation_with_wrong_password(self, register_new_courier_and_return_login_password, delete_courier_by_id):
        login, password, _, courier_id = register_new_courier_and_return_login_password

        payload = {"login": login, "password": password + "_WRONG_PASSWORD",}
        response = requests.post(Api.COURIER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.NOT_FOUND_404
            and response.json()["message"] == ResponseMessage.USER_NOT_FOUND
        )
        delete_courier_by_id(courier_id)
