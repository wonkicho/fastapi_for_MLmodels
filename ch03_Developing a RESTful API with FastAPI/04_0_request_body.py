from enum import Enum
from fastapi import FastAPI, Query, Body


    
app = FastAPI()

"""
Body
문서 및 파일과 같은 양식 제출을 나타내는 HTTP 요청 일부분
REST API에서는 json으로 인코딩, db에 구조화된 객체 만드는데 사용됨
"""
@app.post("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name" : name, "age" : age}