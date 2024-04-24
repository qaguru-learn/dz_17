from dataclasses import dataclass


@dataclass
class User:
    id: int = 2
    wrong_id: int = 0
    name: str = 'Neo'
    wrong_name: int = 0
    job: str = 'TheOne'
    new_job: str = 'Programmer'
    email: str = 'eve.holt@reqres.in'
    password: str = 'cityslicka'
