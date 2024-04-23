from pydantic import BaseModel
from datetime import datetime


class PostUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


"""
{
    "name": "morpheus",
    "job": "leader",
    "id": "725",
    "createdAt": "2024-04-23T16:14:06.119Z"
}
"""