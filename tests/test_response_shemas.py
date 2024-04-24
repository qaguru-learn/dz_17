import pytest
import allure
import requests
from src.models.get_response import GetUserResponse, GetListUsersResponse
from src.models.post_response import RegisterUserResponse, CreateUserResponse
from data.constant import User


@pytest.mark.positive
@pytest.mark.smoke
class TestPositiveResponseShemas:
    
    @allure.description('Проверка схемы ответа на запрос GET получение данных пользователя. Позитивный сценарий. В ответе статус 200 и валидный json')
    def test_response_get_user(self):
        with allure.step(f'Создание запроса. Получение пользователя по ID {User.id}'):
            response = requests.get(f'https://reqres.in/api/users/{User.id}')

        with allure.step('Проверка статуса. Ожидается статус 200'):
            assert response.status_code == 200, "Статус код должен равняться 200"
        
        with allure.step('Проверка валидного содержания. Ожидается json с данными пользователя'):
            assert GetUserResponse(**response.json()), "Содержание должно соответствовать схеме ответа GetUserResponse"
    
    @allure.description('Проверка схемы ответа на запрос POST создание пользователя. Позитивный сценарий. В ответе статус 201 и валидный json')
    def test_response_post_user(self):
        with allure.step(f'Создание запроса. Создание пользователя {User.name}, {User.job}'):
            response = requests.post('https://reqres.in/api/users', json={'name': User.name, 'job': User.job})
            
        with allure.step('Проверка статуса. Ожидается статус 201'):
            assert response.status_code == 201, "Статус код должен равняться 201"
        
        with allure.step('Проверка валидного содержания. Ожидается json с данными пользователя'):
            assert CreateUserResponse(**response.json()), "Содержание должно соответствовать схеме ответа CreateUserResponse"
    
    @allure.description('Проверка схемы ответа на запрос GET получение списка пользователей. Позитивный сценарий. В ответе статус 200 и валидный json')
    def test_response_get_list_users(self):
        with allure.step(f'Создание запроса. Получение списка пользователей'):
            response = requests.get('https://reqres.in/api/users?page=2')
            
        with allure.step('Проверка статуса. Ожидается статус 200'):
            assert response.status_code == 200, "Статус код должен равняться 200"
        
        with allure.step('Проверка валидного содержания. Ожидается json с данными пользователя'):
            assert GetListUsersResponse(**response.json()), "Содержание должно соответствовать схеме ответа GetListUsersResponse"
    
    @allure.description('Проверка схемы ответа на запрос POST регистрация аккаунта. Позитивный сценарий. В ответе статус 200 и валидный json')
    def test_response_register_account(self):
        with allure.step(f'Создание запроса. Регистрация аккаунта {User.email}, {User.password}'):
            response = requests.post('https://reqres.in/api/register', json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
            
        with allure.step('Проверка статуса. Ожидается статус 200'):
            assert response.status_code == 200, "Статус код должен равняться 200"
        
        with allure.step('Проверка валидного содержания. Ожидается json с данными пользователя'):
            assert RegisterUserResponse(**response.json()), "Содержание должно соответствовать схеме ответа RegisterUserResponse"
