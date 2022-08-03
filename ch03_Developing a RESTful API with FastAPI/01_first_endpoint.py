from fastapi import FastAPI

app = FastAPI()

#excute : uvicorn 01_first_endpoint:app

@app.get("/")
async def hello_world():
    return {"hello" : "world"}