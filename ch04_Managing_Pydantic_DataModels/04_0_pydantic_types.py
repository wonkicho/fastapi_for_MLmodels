from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

try: 
    #User(email="jdoe", website="https://www.example.com")
    User(email="jdoe@example.com", website="https://www.example.com")
except ValidationError as e:
    print(str(e))

