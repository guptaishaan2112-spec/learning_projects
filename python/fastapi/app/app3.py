from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import postcreate,postreturn, UserCreate, UserRead, UserUpdate
from app.db import Post, create_db_and_tables, get_async_session, User
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.images import imagekit
from imagekitio import ImageKit
import shutil
import os
import uuid 
import tempfile
from app.users import auth_backend, fastapi_users, current_active_user

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(fastapi_users.get_auth_router(auth_backend),prefix='auth/jwt',tags=['auth'])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix= '/auth', tags=['auth'])
app.include_router(fastapi_users.get_reset_password_router(), prefix='/auth', tags = ['auth'])
app.include_router(fastapi_users.get_verify_router(UserRead), prefix='/auth', tags = ['auth'])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix='/users', tags = ['users'])
@app.post('/upload')
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(''),
    user: User = Depends(current_active_user),
    session:AsyncSession = Depends(get_async_session)
):
    temp_file_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False,suffix=os.path.splitext(file.filename)[1]) as temp_file:   
                temp_file_path = temp_file.name# .name gives the path of the file which is temp_file in this case
                shutil.copyfileobj(file.file,temp_file)# file is the variable name and .file is the attribute of UploadFile 
        upload_result = imagekit.upload_file(
             file = open(temp_file_path,'rb'),
             file_name = file.filename,
             options=UploadFile(
                  use_unique_file_name=True, # add something in the end of the file name incase it matches another one and thus ensure uniqueness
                  tags = ['backend-upload'] # you can access the photos stored in img kit db via the tag 'backend upload'
             )
        )
        if upload_result.response_metadata.http_status_code == 200:
            post = Post(    # Post --> class in which the table is stored 
                caption = caption,
                url = upload_file.url,#.url is a built in att in imagekit you dont have to define it
                file_type = 'video' if file.content_type.startswith('video/') else 'image',
                file_name = upload_result.name # .name is a built in att in python you dont have to define it
            ) 
            session.add(post)  # adding a session is like staging a task in github
            await session.commit()#commitiing is like a commit command in github and save the changes in the db
            await session.refresh(post)#commit() writes the row to the database (including generated values) but python does not know about it. refresh() reads those values back into the Python object.
            return post
    except:
         pass
    finally:
         if temp_file_path and os.path.exists(temp_file_path):# it checks if the temp file was created and still exists
            os.unlink(temp_file_path)# it will delete the temp file that stores the img
         file.file.close()
@app.get('/feed')
async def get_feed(
    session:AsyncSession=Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))# basically select * from Posts;   [Posts--> (table)] we use Post(class in which table is stored) as arg in select as it represents the table 
    posts = [row[0] for row in result.all()]
# result.all() converts all result into a list
# [
#     (Post(...),),
#     (Post(...),)
# ]
# [
#     (Post(id=1, caption="Hello"),),
#     (Post(id=2, caption="World"),),
# ]
# row[0] --> Post(id=1, caption="Hello")
    result = await session.execute(select(User))
    users = [row[0] for row in result.all()]
    user_dict = {u.id: u.email for u in users}
    posts_data=[]
    for post in posts:
        posts_data.append(
            {
                'id':str(post.id),
                'user_id': str(post.user_id),
                'capiton':post.caption,
                'url':post.url,
                'file_type':post.file_type,
                'file_name':post.file_name,
                'created_at':post.created_at,
                'is_owner':post.user_id == user.id,
                'email': user_dict.get(post.user_id)
            }
        )
        return posts_data
@app.delete('/posts/{post_id}')
async def delete_post(post_id:str, session: AsyncSession = Depends(get_async_session),user: User = Depends(current_active_user),):
     try:
          post_uuid = uuid.UUID(post_id)# since our id is stored as UUID in the table therefore we use UUID() to convert the str post_id into UUID
          result = await session.execute(select(Post).where(Post.id == post_uuid))# here result is not a post or a list of posts it is an object that contains the querry result like:-
# [
#     (Post(id=123, caption="Cat", file_name="cat.jpg"),),
#     (Post(id=123, caption="Dog", file_name="dog.jpg"),)
# ] 
# i have assumed two posts with same id for better understanding of whats happening although it cant happen due to the unique constraint
          post = result.scalars().first()#scalar basically unpacks the value stored in results and first chooses the first unpacked value 
#after using this line we have something like this:-
# Post(id=123, caption="Cat", file_name="cat.jpg")
# Post(id=123, caption="Dog", file_name="dog.jpg")
# and .first will now choose the first unpacked post ie the one with cat.jpg
          await session.delete(post)
          await session.commit()
          return {'success':True,'message':'post deleted successfully'}
          if post.user_id != user.id:
               raise HTTPException(status_code=403, detail='you dont have permission to delete this post')
     except HTTPException as e:# in case post is not present 
          raise e
     except Exception as e:# other exception
          raise HTTPException(status_code=500, detail=str(e))
     


     # WAHAT DOES INLUDE_ROUTER DO??
# =========================== ROUTERS =============================
# A Router is simply a collection of API endpoints.
#
# Instead of writing every route manually, FastAPI Users already
# provides routers for common authentication features.
#
# include_router() attaches those routes to our application.
#
# Example:
#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt"
# )
#
# creates endpoints like:
#
# POST /auth/jwt/login
# POST /auth/jwt/logout
#
# prefix
#     Adds the same beginning to every endpoint in the router.
#
# tags
#     Only groups endpoints in Swagger documentation.
#     It does NOT affect application logic.
#
# Available routers:
#
# get_auth_router()
#     -> Login / Logout
#
# get_register_router()
#     -> Register new users
#
# get_reset_password_router()
#     -> Forgot password / Reset password
#
# get_verify_router()
#     -> Email verification
#
# get_users_router()
#     -> Get/update current user information
# ================================================================