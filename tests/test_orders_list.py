import allure
import pytest
import requests

from data import Data, StatusCode, Api


class TestOrdersListing:
    @pytest.mark.parametrize('order_page_params', Data.ORDER_PAGE_PARAMS)
    @allure.title('Тестирование вывода списка заказов')
    @allure.description(
        "Параметризуем лимиты и номера страниц, выводим доступные заказы для взятия курьерами"
    )
    def test_list_all_available_orders(self, order_page_params):
        limit = order_page_params["limit"]
        page = order_page_params["page"]

        url = f"{Api.ORDERS_LIST}?limit={limit}&page={page}"
        response = requests.get(url)

        assert (
            response.status_code == StatusCode.OK_200
            and response.json()["orders"] is not None
        )
