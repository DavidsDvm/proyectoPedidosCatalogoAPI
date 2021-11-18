from typing import Optional
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str