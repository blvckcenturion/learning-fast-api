from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, DateTime
from database import Base


class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    status = Column(String(1), default="1")
    likes = Column(Integer, default=0)
