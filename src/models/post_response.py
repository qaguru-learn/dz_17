from pydantic import BaseModel
from datetime import datetime


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class RegisterUserResponse(BaseModel):
    id: int
    token: str
    