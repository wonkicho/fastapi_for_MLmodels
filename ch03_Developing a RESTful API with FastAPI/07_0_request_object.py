from fastapi import FastAPI, Request

app = FastAPI()

"""
    클라이언트에 의해 전송되는 메시지를 요청(requests)이라 하고, 요청에 대해 서버에서 응답으로 전송하는 메시지를 응답(responses)이라고 한다.
"""

@app.get("/")
async def get_request_object(request:Request):
    return {'path' : request.url.path}

