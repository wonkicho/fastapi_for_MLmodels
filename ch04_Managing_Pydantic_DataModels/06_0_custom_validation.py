from datetime import date
from pydantic import BaseModel, validator

"""
Validator는 정적 클래스 메서드
v 변수는 검증할 값
"""

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator("birthdate")
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age =delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return v