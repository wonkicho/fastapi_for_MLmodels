from fastapi import FastAPI, status
from pydantic import BaseModel

class PublicPost(BaseModel):
    title: str
    
    
app = FastAPI()

posts = {
    1 : PublicPost(title="Hello")
}

@app.get("/posts/{id}", response_model=PublicPost)
async def get_post(id: int):
    return posts[id]