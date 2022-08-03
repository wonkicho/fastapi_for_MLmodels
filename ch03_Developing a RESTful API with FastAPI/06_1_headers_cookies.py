from fastapi import FastAPI, Header

app = FastAPI()

#HTTP 헤더는 클라이언트와 서버가 요청 또는 응답으로 부가적인 정보를 전송할 수 있도록 해줍니다
@app.get("/")
async def get_header(user_agent : str = Header(...)):
    return {'user_agent' : user_agent}