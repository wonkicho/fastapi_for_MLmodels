from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

def list_factory():
    return ["a", "b", "c"]

#default_factory에는 모델 인스턴스화 중 호출되는 함수 전달해야함
class Model(BaseModel):
    l: List[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: List[str] = Field(default_factory=list)