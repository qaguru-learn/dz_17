from pydantic import BaseModel, field_validator
import re


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator('email')
    def validate_email(cls, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('email must be a valid email address')
        return email

    @field_validator('avatar')
    def validate_url(cls, value):
        if not value.startswith('https://'):
            raise ValueError('url must start with https://')
        return value


class Support(BaseModel):
    url: str
    text: str

    @field_validator('url')
    def validate_url(cls, value):
        if not value.startswith('https://'):
            raise ValueError('url must start with https://')
        return value


class GetUserResponse(BaseModel):
    data: User
    support: Support


user_schema = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

print(GetUserResponse(**user_schema))
