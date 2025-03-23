
from data import Data, StatusCode, Api
import allure
from base_test import BaseTest
import json
import pytest


class TestOrderCreation(BaseTest):
    @pytest.mark.parametrize('order_data', Data.order_data())
    @allure.title('Тестирование создания заказа')
    @allure.description(
        "Тестируется успешное создание заказа с передачей как обязательных полей, "
        "так и не обязательного поля color. "
        "В файле с параметрами 6 вариантов: "
        "- с полем color=BLACK, "
        "- с полем color=BLACK и GREY,"
        "- без поля color"
    )
    def test_order_successful_creation(self, order_data):
        response = self.post_request(Api.ORDERS, json.dumps(order_data))

        assert (
            response.status_code == StatusCode.CREATED_201
            and isinstance(response.json()["track"], int)
        )
