import requests
import random
import string
import pytest
from data import Api


@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

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

    return login_pass


@pytest.fixture(scope="function")
def generate_random_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return login, password, first_name


@pytest.fixture(scope="function")
def delete_courier_by_id():
    def _delete_courier_by_id(courier_id):
        requests.delete(f"{Api.COURIER}/{courier_id}")

    return _delete_courier_by_id
