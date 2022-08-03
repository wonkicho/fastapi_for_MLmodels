from fastapi import FastAPI, Response

app = FastAPI()

"""
응답 개체를 사용하면 헤더를 포함한 속성 집합에 액세스할 수 있습니다. 
키는 헤더의 이름이고 값은 연관된 값인 간단한 사전입니다. 
따라서 사용자 지정 헤더를 직접 설정하는 것이 비교적 간단합니다.

 content-length: 17 
 content-type: application/json 
 custom-header: Custom-Header-Value 
 date: Sat,30 Jul 2022 14:27:46 GMT 
 server: uvicorn 

"""

@app.get("/")
#http://127.0.0.1:8000/docs#/default/custom_header__get
async def custom_header(response : Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello" : "world"}