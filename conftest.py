import requests
from helpers import generate_random_string
import pytest
from data import Api


@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():
    login_pass = []
    courier_id = None

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Api.COURIER, data=payload)

    if response.status_code == 201:
        courier_id = requests.post(
            Api.COURIER_LOGIN,
            data={"login": login, "password": password}
        ).json()["id"]

        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
        login_pass.append(courier_id)

    yield login_pass

    if response.status_code == 201 and courier_id is not None:
        # Финализатор для удаления созданного курьера
        requests.delete(f"{Api.COURIER}/{courier_id}")


@pytest.fixture(scope="function")
def generate_random_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return login, password, first_name
