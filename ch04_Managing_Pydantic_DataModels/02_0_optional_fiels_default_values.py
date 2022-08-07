from typing import Optional
from pydantic import BaseModel

#Optional 사용 시 None 값 할당 가능
class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = None
    subscribed_newsletter: bool = True

user = UserProfile(nickname='jdoe')
print(user)