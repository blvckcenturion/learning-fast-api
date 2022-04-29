from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, DateTime
from database import Base

class Restaurant(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    content = Column(Text)
    created_at = Column(DateTime)
    status = Column(String(1))
    likes = Column(Integer)