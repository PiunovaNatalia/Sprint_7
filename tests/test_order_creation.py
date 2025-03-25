import allure
import json
import pytest
import requests

from data import Data, StatusCode, Api


class TestOrderCreation:
    @pytest.mark.parametrize('order_data', Data.ORDERS_TEST_DATA)
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
        response = requests.post(Api.ORDERS, data=json.dumps(order_data))

        assert (
            response.status_code == StatusCode.CREATED_201
            and isinstance(response.json()["track"], int)
        )
