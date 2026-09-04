from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column,Text,String,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship 
from datetime import datetime
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTableUUID
from fastapi import Depends
database_url = 'sqlite+aiosqlite:///./test.db'
# sqlite --> use sqlite db
# + aiosqlite --> use sqlite with the aiosqlite asyn driver 
# :/// --> separates the db location from the connection info
#./test.db --> location of the db and '.' indicates the current location
class Base(DeclarativeBase):
    pass
class User(SQLAlchemyBaseUserTableUUID, Base):
    posts = relationship(argument='Post',back_populates='user') # Post is the name of class you want to connect, so now User class is connected to Post class.
    # back_populates means that the opposite side of this relationship is called user (in post there is a relationship stored in 'user' obj) 
    # this line creates a python attribute user.posts
class Post(Base):
#DeclarativeBase is the foundation class that tells SQLAlchemy:
#"Any class that inherits from me is a database model. Read its columns and relationships so you can map it to a database table."
    __tablename__='Posts'

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)#as_uuid = True generate a random unique id for each row
    # with as_UUID = True the class of id is UUID and without as_UUID the class of the uuid is str
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'),nullable=False) # created a foreign key which references the id of a user 
    caption = Column(Text)
    url = Column(String, nullable=False) # nullable = false means that this column's value cannot be null
#diff b/w text and string --> major diff is that text can store unlimited length of str however string can only store upto a certain characters like 100 and you may specify max char in str by writing String(100) --> this will take max 100 char
    file_type = Column(String,nullable=False)
    file_name = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    user = relationship(argument='User', back_populates='posts')# this line creates a python attribute posts.user

engine = create_async_engine(database_url)   
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # this function basically just creates every table in which the class inherits from DeclarativeBase in the db
async def get_async_session() -> AsyncGenerator[AsyncSession,None]:
    async with async_session_maker() as session:
        yield session
        # this function will allow us to access the data from the database
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)



    # NOTES ON RELATIONSHIP FUNCTION
# ========================= RELATIONSHIPS =========================
# A relationship() creates a Python-level link between two models.
# It DOES NOT create a database column. The ForeignKey does that.
#
# Example:
#
# User (1) ---------------------> (*) Post
#
# One user can have many posts.
# One post belongs to exactly one user.
#
# Therefore:
#
# User model:
#     posts = relationship("Post", back_populates="user")
#
#     user.posts
#     -> Returns all Post objects belonging to that user.
#
# Post model:
#     user = relationship("User", back_populates="posts")
#
#     post.user
#     -> Returns the User object that owns this post.
#
# back_populates tells SQLAlchemy that these two relationship
# attributes represent the SAME relationship.
#
# Because of this, SQLAlchemy automatically keeps them synchronized.
#
# Example:
#
# post.user = user
#
# automatically updates
#
# user.posts
#
# and vice versa.
#
# ForeignKey stores the relationship in the database.
# relationship() lets Python easily navigate between objects.
# ================================================================