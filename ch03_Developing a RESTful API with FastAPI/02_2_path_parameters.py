from enum import Enum
from fastapi import FastAPI

#string, Enum class 상속
class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"
    
#main app
app = FastAPI()    

@app.get("/users/{type}/{id}/")
async def get_user(type : UserType, id : int):
    return {"type" : type, "id" : id}