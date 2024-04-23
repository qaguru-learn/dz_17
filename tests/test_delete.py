import allure
import pytest
import requests
from data.constant import User
from src.errors import WrongStatusCode


@allure.description(
    'Удаление пользователя. Позитивный сценарий. возвращается статус 204 и пустоe тело ответа'
)
@pytest.mark.positive
def test_positive_delete_user():
    with allure.step(f'Создание запроса. Удаление пользователя по ID {User.id}'):
        response = requests.delete(f'https://reqres.in/api/users/{User.id}')

    with allure.step('Проверка статуса. Ожидается статус 204'):
        assert response.status_code == 204, \
            "Статус код должен быть 204"

    with allure.step('Проверка содержания. Ожидается пустое тело ответа'):
        assert not response.content, \
            "Содержание тела ответа должно быть пустым"


@allure.description(
    'Удаление пользователя. Негативный сценарий. Возвращается статус 404 и не пустое тело ответа'
)
@pytest.mark.negative
@pytest.mark.xfail(
    reason="В API ответ успешный при подстановке некорректного имени. Баг, а не фича!"
)
@pytest.mark.parametrize('wrong_id', [User.wrong_id, -10, '', None, 'wrong_id'])
def test_negative_delete_user(wrong_id):
    with allure.step(f'Создание запроса. Удаление пользователя по ID {wrong_id}'):
        response = requests.delete(f'https://reqres.in/api/users/{wrong_id}')

    with allure.step('Проверка статуса. Ожидается статус 404'):
        try:
            assert response.status_code == 404, \
                "Статус код должен быть 404"
        except AssertionError:
            raise WrongStatusCode(response.status_code, 404)

    with allure.step('Проверка содержания. Ожидается не пустое тело ответа'):
        try:
            assert response.content, \
                "Содержание тела ответа должно быть не пустым"
        except AssertionError:
            raise ValueError("Содержание тела ответа должно быть не пустым")
