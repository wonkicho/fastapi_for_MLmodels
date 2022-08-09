from pydantic import BaseModel
from fastapi import FastAPI, status


class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int = 0

app = FastAPI()

@app.post("/posts", status_code = status.HTTP_201_CREATED, response_model = PostPublic)
async def create(post_create: PostCreate):
    new_id = max(db.posts.key() or (0,)) + 1

    post = PostDB(id = new_id, **post_create.dict())
    db.posts[new_id] = post
    return post