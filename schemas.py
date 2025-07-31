from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class UserData(BaseModel):
    username: str
    email: str
    password: str


class ReadUserData(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        from_attributes = True




class PostLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutUserDataId(BaseModel):
    id: Optional[Any]=None
    username: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True



class PostUserData(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True



class PostCreateUser(BaseModel):
    username: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

