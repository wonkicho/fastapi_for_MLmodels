from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    
class Company(BaseModel):
    name: str
    
app = FastAPI()

#pydantic BaseModel 선언
#모든 모델이 상속받아햐하는 기본 클래스

@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user" : user, "company" : company}