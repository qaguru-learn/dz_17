import allure
import pytest
import requests
from src.errors import WrongStatusCode, WrongJson
from data.constant import User
from src.models.put_response import PutUserResponse


@allure.description(
    'Изменение пользователя. Позитивный сценарий. возвращается статус 200 и json с новыми данными пользователя'
)
@pytest.mark.positive
def test_positive_update_user():
    with allure.step(f'Создание запроса. Изменение пользователя по ID {User.id}'):
        response = requests.put(f'https://reqres.in/api/users/{User.id}', json={'name': User.name, 'job': User.new_job})

    with allure.step('Проверка статуса. Ожидается статус 200'):
        assert response.status_code == 200, \
            "Статус код должен быть 200"

    with allure.step('Проверка формы ответа. Ожидается json с новыми данными пользователя'):
        assert PutUserResponse(**response.json()), \
            "Содержание должно соответствовать схеме ответа PutUserResponse"

    with allure.step('Проверка соответствия содержимого ответа'):
        response_json = response.json()
        response_user_name = response_json['name']
        response_user_job = response_json['job']
        assert response_user_name == User.name, \
            f"Соответствие имени пользователя в ответе {response_user_name} имени в запросе {User.name}"
        assert response_user_job == User.new_job, \
            f"Соответствие должности пользователя в ответе {response_user_job} должности в запросе {User.new_job}"


@allure.description(
    'Изменение пользователя. Негативный сценарий. возвращается статус 400 и сообщение об ошибке'
)
@pytest.mark.negative
@pytest.mark.parametrize('wrong_job', [0, -10, '', None, {}])
@pytest.mark.xfail(
    reason="В API есть возможность изменять job пользователя на любой набор символов, включая пустую строку."
           + " Баг, а не фича!"
)
def test_negative_update_user(wrong_job):
    with allure.step(f'Создание запроса. Изменение пользователя по ID {User.id} с некорректным именем {wrong_job}'):
        response = requests.put(
            f'https://reqres.in/api/users/{User.id}', json={'name': wrong_job, 'job': User.new_job})

    with allure.step('Проверка статуса. Ожидается статус 400'):
        try:
            assert response.status_code == 400, \
                "Статус код должен равняться 400"
        except AssertionError:
            raise WrongStatusCode(response.status_code, 400)

    with allure.step('Проверка содержания. Ожидается пустой json'):
        try:
            assert response.json() == {}, \
                "Содержание должно соответствовать пустому json"
        except AssertionError:
            raise WrongJson(response.json(), {})
