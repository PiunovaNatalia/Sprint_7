
from data import ResponseMessage, StatusCode, Api
import allure
from base_test import BaseTest

class TestCourierLogin(BaseTest):
    @allure.title('Тестирование авторизации курьера')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться"
    )
    def test_courier_authorisation(self):
        login, password, _ = self.get_new_courier()

        payload = {"login": login, "password": password}
        response = self.post_request(Api.COURIER_LOGIN, payload)

        assert (
            response.status_code == StatusCode.OK_200
            and isinstance(response.json()["id"], int)
        )

    @allure.title('Тестирование авторизации курьера без пароля')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться без пароля"
    )
    def test_courier_authorisation_without_password(self):
        login, _, _ = self.get_new_courier()

        payload = {"login": login, "password": ""}
        response = self.post_request(Api.COURIER_LOGIN, payload)

        assert (
            response.status_code == StatusCode.BAD_REQUEST_400
            and response.json()["message"] == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN
        )

    @allure.title('Тестирование авторизации курьера без логина')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться без логина"
    )
    def test_courier_authorisation_without_login(self):
        _, password, _ = self.get_new_courier()

        payload = {"login": "", "password": password}
        response = self.post_request(Api.COURIER_LOGIN, payload)

        assert (
            response.status_code == StatusCode.BAD_REQUEST_400
            and response.json()["message"] == ResponseMessage.REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN
        )

    @allure.title('Тестирование авторизации курьера с несуществующим логином')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться с несуществующим логином"
    )
    def test_courier_authorisation_with_wrong_login(self):
        login, password, _ = self.get_new_courier()

        payload = {"login": login + "_WRONG_LOGIN", "password": password}
        response = self.post_request(Api.COURIER_LOGIN, payload)

        assert (
            response.status_code == StatusCode.NOT_FOUND_404
            and response.json()["message"] == ResponseMessage.USER_NOT_FOUND
        )

    @allure.title('Тестирование авторизации курьера с неправильным паролем')
    @allure.description(
        "Создаем нового курьера для проверки авторизации "
        "и пытаемся авторизоваться с неправильным паролем"
    )
    def test_courier_authorisation_with_wrong_password(self):
        login, password, _ = self.get_new_courier()

        payload = {"login": login, "password": password + "_WRONG_PASSWORD",}
        response = self.post_request(Api.COURIER_LOGIN, payload)

        assert (
            response.status_code == StatusCode.NOT_FOUND_404
            and response.json()["message"] == ResponseMessage.USER_NOT_FOUND
        )