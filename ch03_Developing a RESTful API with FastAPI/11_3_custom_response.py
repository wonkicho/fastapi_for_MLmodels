import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/cat")
async def get_cat():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    picture_path = os.path.join(root_dir, "assets", "cat.jpg")
    
    return FileResponse(picture_path)