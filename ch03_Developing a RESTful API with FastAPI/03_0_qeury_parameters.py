from fastapi import FastAPI, Path


app = FastAPI()

#http://127.0.0.1:8000/users?page=5&size=50
@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page" : page, "size" : size}

