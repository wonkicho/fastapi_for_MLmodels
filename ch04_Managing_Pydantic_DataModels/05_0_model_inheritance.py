from pydantic import BaseModel

#모델 상속

#데이터 생성 시 
class PostCreate(BaseModel):
    title: str
    content: str

#게시된 데이터
class PostPublic(BaseModel):
    id: int
    title: str
    content: str

#DB에 모두 맘길 데이터 형태
class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0