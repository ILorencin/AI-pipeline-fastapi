from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

#pydantic se i dalje koristi bez obzira na sqlalchemi kako bi se oblikovao request

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_model = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str



class PostBase(BaseModel):
    title: str
    content: str 
    published: bool = True 


class PostCreate(PostBase):
    pass 

class PostResponse(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_model = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_model = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)# da moze biti samo 0 ili 1