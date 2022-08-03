from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

@app.get("/")
async def get_cookie(hello : Optional[str] = Cookie(None)):
    return {'hello' : hello}