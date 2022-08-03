from fastapi import FastAPI

#main app
app = FastAPI()

#root path + /users/id 값
@app.get("/users/{id}")
async def get_user(id: int):
    return {"id" : id}


"""
Rest API의 목적은 데이터와 상호작용할 수 있는 구조화된 방법을 제공
path, query, payload 등 response 정의 하기 위해 정보 보내는 것 중요함

모든 매개변수를 선언적으로 정의할 수 있음
"""