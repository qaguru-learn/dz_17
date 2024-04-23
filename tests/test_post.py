import requests
from data.constant import User
import allure
import pytest
from src.models.post_response import PostUserResponse
from src.errors import WrongStatusCode, WrongJson


@allure.description(
    'Создание пользователя. Позитивный сценарий. возвращается статус 201 и json с данными пользователя'
)
@pytest.mark.positive
def test_positive_create_user():
    with allure.step(f'Создание запроса. Создание пользователя {User.name}'):
        response = requests.post('https://reqres.in/api/users', json={'name': User.name, 'job': User.job})

    with allure.step('Проверка статуса. Ожидается статус 201'):
        assert response.status_code == 201, \
            "Статус код должен равняться 201"

    with allure.step('Проверка содержания. Ожидается json с данными пользователя'):
        assert PostUserResponse(**response.json()), \
            "Содержание должно соответствовать схеме ответа PostUserResponse"

    with allure.step('Проверка соответствия содержимого ответа'):
        response_json = response.json()
        response_user_name = response_json['name']
        response_user_job = response_json['job']
        assert response_user_name == User.name, \
            f"Соответствие имени пользователя в ответе {response_user_name} имени в запросе {User.name}"
        assert response_user_job == User.job, \
            f"Соответствие должности пользователя в ответе {response_user_job} должности в запросе {User.job}"


@allure.description(
    'Создание пользователя. Негативный сценарий. возвращается статус 400 и сообщение об ошибке'
)
@pytest.mark.xfail(
    reason="В API есть возможность создавать пользователя с именем из любого набора символов, включая пустую строку."
           + " Баг, а не фича!"
)
@pytest.mark.negative
@pytest.mark.parametrize('wrong_name', [User.wrong_name, -10, '', None])
def test_negative_create_user(wrong_name):
    with allure.step(f'Создание запроса. Создание пользователя с некорректным именем {wrong_name}'):
        response = requests.post('https://reqres.in/api/users', json={'name': wrong_name, 'job': User.job})

    with allure.step('Проверка статуса. Ожидается статус 400'):
        try:
            assert 400 == 400, \
                "Статус код должен равняться 400"
        except AssertionError:
            raise WrongStatusCode(response.status_code, 400)

    with allure.step('Проверка содержания. Ожидается пустой json'):
        try:
            assert response.json() == {}, \
                "Содержание должно соответствовать пустому json"
        except AssertionError:
            raise WrongJson(response.json(), {})
