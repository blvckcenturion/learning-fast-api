from datetime import datetime
from pydantic import BaseModel

class PostIn(BaseModel):
    username: str
    content: str

    class Config:
        orm_mode = True

class Content(BaseModel):
    content: str