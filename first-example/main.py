# Simplest fastAPI server
# Simple Posts CRUD API using MySQL local instance and ORM

# Posts
# Create Post
# Get Post by ID
# Get Post by status
# Get Posts
# Update Post
# Like a Post
# Delete Post
import model
from database import SessionLocal, engine
from fastapi import FastAPI, Request, Form, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schema import PostIn
from typing import Optional
from schema import PostIn
from enum import Enum
from pydantic import BaseModel

model.Base.metadata.create_all(bind=engine)

class Status(str, Enum):
    deleted = 0
    active = 1
    all = 2

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

def get_post(post_id: int, db: Session):
    post = (
        db.query(model.Post)
        .filter(model.Post.id == post_id, model.Post.status == Status.active.value)
        .first()
    )
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/post")
def read_post(
    db: Session = Depends(get_database_session), status: Optional[Status] = Query(Status.active, include_in_schema=False)
):
    db_query = db.query(model.Post)
    if status == Status.all:
        records = db_query.all()
    else: 
        records = db_query.filter(model.Post.status == status.value).all()
    return records


@app.get("/post/{id}")
def read_post(id: int, db: Session = Depends(get_database_session)):
    record = get_post(id, db)
    return record


@app.post("/post")
async def create_post(post: PostIn, db: Session = Depends(get_database_session)):
    db_post = model.Post(**post.dict())
    print(db_post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.patch("/post/{id}")
async def update_post(
    id: int, content: str, db: Session = Depends(get_database_session)
):
    db_post = get_post(id, db)
    db_post.content = content
    db.commit()
    db.refresh(db_post)
    return db_post


@app.patch("/post/{id}/like")
async def like_post(id: int, db: Session = Depends(get_database_session)):
    db_post = get_post(id, db)
    db_post.likes += 1
    db.commit()
    db.refresh(db_post)
    return db_post


@app.delete("/post/{id}")
async def delete_post(id: int, db: Session = Depends(get_database_session)):
    post = get_post(id, db)
    post.status = Status.deleted.value
    db.commit()
    return {"message": "Post deleted"}
