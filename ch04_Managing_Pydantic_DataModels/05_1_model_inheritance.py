from pydantic import BaseModel

#클래스 내 동일 속성 사용시 중복되는 문제가 생김
#상속을 통해서 해결

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