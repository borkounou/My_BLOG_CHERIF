from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional


class Posts(BaseModel):
    title: str
    subtitle: str
    author: str
    contents: str
    date: Optional[datetime] =None


class Hobbies(BaseModel):
    sports: dict = Field(default={})
    travel: dict = Field(default={})
    reading:dict = Field(default={})


