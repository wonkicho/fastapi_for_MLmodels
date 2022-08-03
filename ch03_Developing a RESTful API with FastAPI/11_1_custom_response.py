from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse

app = FastAPI()

#client -> 서버로 요청 -> client로 다시 리다이렉션
@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url")