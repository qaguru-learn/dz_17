from src.models.get_response import GetUserResponse
import allure
import pytest
import requests
from data.constant import User


@allure.description(
    'Получение пользователя по ID. Позитивный сценарий. возвращается статус 200 и json с данными пользователя'
)
@pytest.mark.positive
def test_positive_get_user():
    with allure.step(f'Создание запроса. Получение пользователя по ID {User.id}'):
        response = requests.get(f'https://reqres.in/api/users/{User.id}')

    with allure.step('Проверка статуса. Ожидается статус 200'):
        assert response.status_code == 200, \
            "Статус код должен равняться 200"

    with allure.step('Проверка содержания. Ожидается json с данными пользователя'):
        assert GetUserResponse(**response.json()), \
            "Содержание должно соответствовать схеме ответа GetUserResponse"


@allure.description(
    'Получение пользователя по ID. Негативный сценарий. возвращается статус 404 и сообщение об ошибке'
)
@pytest.mark.negative
def test_negative_get_user():
    with allure.step(f'Создание запроса. Получение пользователя по ID {User.wrong_id}'):
        response = requests.get(f'https://reqres.in/api/users/{User.wrong_id}')

    with allure.step('Проверка статуса. Ожидается статус 404'):
        assert response.status_code == 404, \
            "Статус код должен равняться 404"

    with allure.step('Проверка содержания. Ожидается пустой json'):
        assert response.json() == {}, \
            "Содержание должно соответствовать пустому json"
