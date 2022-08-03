from fastapi import FastAPI

#main app
app = FastAPI()


#다양한 path 타입 정의도 가능
@app.get("/users/{type}/{id}")
async def get_user(type : str, id : int):
    return {"type" : type, "id" : id}