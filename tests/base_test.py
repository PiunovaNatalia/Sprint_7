import requests
from confest import generate_random_courier_data, register_new_courier_and_return_login_password
import allure


class BaseTest:
    @allure.step("Генерируем случайные данные курьера")
    def generate_random_courier_data(self):
        return generate_random_courier_data()

    @allure.step("Выполняем GET-запрос по адресу {url}")
    def get_request(self, url):
        return requests.get(url)

    @allure.step("Выполняем POST-запрос по адресу {url} с параметрами {payload}")
    def post_request(self, url, payload):
        return requests.post(url, data=payload)

    @allure.step("Создаем нового курьера")
    def get_new_courier(self):
        return register_new_courier_and_return_login_password()