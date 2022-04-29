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
import schema
import model
from database import SessionLocal, engine
from enum import Enum
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

model.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db = get_database_session()

app = FastAPI()


