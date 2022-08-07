from datetime import date
from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]

try:
    Person(
        first_name = "John",
        last_name = "Doe",
        gender = "INVALID_VALUE",
        birthdate="1991-01-01",
        interests = ["travel", "sports"],
    )
except ValidationError as e:
    print(str(e))