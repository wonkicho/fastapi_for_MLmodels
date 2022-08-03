from enum import Enum
from fastapi import FastAPI, Query

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"
    
app = FastAPI()

#Query를 통해 동적 매개변수를 url에 추가
@app.get("/users")
async def get_user(page:int = Query(1, gt=0), size : int = Query(10, le=100)):
    return {"page" : page, "size" : size}