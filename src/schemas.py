from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    id: int
    identification: str
    name: str
    birthtDay: datetime
    monthBirthtDay: str
    address: str
    cellPhone: str
    email: str
    password: str
    zone: str
    type: str

class CreateCookwareRequest(BaseModel):
    reference: str
    brand: str
    category: str
    materiales: str
    dimensiones: str
    description: str
    availability: bool
    price: int
    quantity: int
    photography: str

class CreateOrderRequest(BaseModel):
    id: int
    registerDay: datetime
    status: str
    salesMan: dict
    products: dict
    quantities: dict