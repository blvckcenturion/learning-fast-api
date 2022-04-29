from datetime import datetime
from pydantic import BaseModel

class Restaurant(BaseModel):
    id = int
    username = str
    content = str
    created_at = datetime
    status = str
    likes = int

    class Config:
        orm_mode = True