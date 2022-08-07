from pydantic import BaseModel

#각 변수에 type을 hint로 주어짐
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int