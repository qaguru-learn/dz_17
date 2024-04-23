from pydantic import BaseModel
from datetime import datetime


class PutUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime
