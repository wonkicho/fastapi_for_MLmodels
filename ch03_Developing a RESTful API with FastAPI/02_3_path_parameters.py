from fastapi import FastAPI, Path


app = FastAPI()

#Path 기능 (fastapi 내장)
#1보다 크거나 같은 id 변수 값만 허용
#문자열 값에 대한 유효성 검사도 가능, 길이 설정 가능
"""
gt: Greater than
ge: Greater than or equal to
lt: Less than
le: Less than or equal to
"""


@app.get("/users/{id}")
async def get_user(id : int = Path(..., ge=1)):
    return {"id" : id}