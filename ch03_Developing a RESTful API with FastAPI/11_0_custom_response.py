from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

"""
response class에 따라서 조합 가능, return 값 원하는대로 response class 만들 수 잇음
"""


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello World!</title>
            </head>
            <body>
                <h1>hello world!</h1>
            </body>
        </html>
    """
    
@app.get("/text", response_class = PlainTextResponse)
async def text():
    return "Hello world!"