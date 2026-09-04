from fastapi import FastAPI, HTTPException
from app.schemas import postcreate,postreturn
from app.db import create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)
posts = {
    1: {"title": "First Post", "content": "This is the content of the first post."},
    2: {"title": "Second Post", "content": "This is the content of the second post."},
    3: {"title": "Third Post", "content": "This is the content of the third post."},
    4: {"title": "Fourth Post", "content": "This is the content of the fourth post."},
    5: {"title": "Fifth Post", "content": "This is the content of the fifth post."},
    6: {"title": "Sixth Post", "content": "This is the content of the sixth post."},
    7: {"title": "Seventh Post", "content": "This is the content of the seventh post."},
    8: {"title": "Eighth Post", "content": "This is the content of the eighth post."},
    9: {"title": "Ninth Post", "content": "This is the content of the ninth post."},
    10: {"title": "Tenth Post", "content": "This is the content of the tenth post."},
}
@app.get("/posts")# get request --> to access the data from the server
def get_posts(limit: int = len(posts)):# query parameter --> it is added in the function and in the url it comes after '?' 
    return list(posts.values())[:limit]
@app.get("/posts/{post_id}") # path parameter --> it is added in the decorator and in the url it comes after '/'
def get_post(post_id: int):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]
@app.post("/posts") # post request --> to send the data to the server
def create_post(post: postcreate)-> postreturn: #postreturn is the response model which is used to specify the data type of output data
    post_id = len(posts) + 1
    new_post = {"title": post.title, "content": post.content}
    posts[post_id] = new_post
    return new_post
# similarly there other requests like put, delete etc. which can be implemented in the same way as above.
