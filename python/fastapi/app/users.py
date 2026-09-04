import uuid
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from fastapi_users.db import SQLAlchemyUserDatabase
from app.db import User, get_user_db
secret = 'ishaanislearningfastapi'# this must not be shared by this someone can decode the jwt tokens and mess with the user db
class UserManager(UUIDIDMixin,BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = secret
    verification_token_secret = secret
    async def on_after_register(self, user: User , request = Optional[Request] = None):
        print(f'user {user.id} has registered')
    async def on_after_forgot_password(self, user: User ,token:str ,request = Optional[Request] = None):
        print(f'user {user.id} has forgot their password. Reset token: {token}')
    async def on_after_request_verify(self, user: User ,token:str ,request = Optional[Request] = None):
        print(f'verification requested for user {user.id}. verification token: {token}')
async def get_user_manager(user_db: SQLAlchemyUserDatabase= Depends(get_user_db)):
    yield UserManager(user_db)
bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')
def get_jwt_strategy():
    return JWTStrategy(secret=secret, lifetime_seconds=3600)
auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
) 
fastapi_users = FastAPIUsers[User,uuid.UUID](get_user_manager,auth_backend:[auth_backends])
current_active_user = fastapi_users.current_user(active=True)


# WHAT'S GOING ON IN THIS FILE(no need to fully understand it ust remember which obj do which thing)
# ========================= USER MODEL ============================(whats happening in the file users.py)
# This file defines how a User is stored in the database.
#
# We inherit from SQLAlchemyBaseUserTableUUID instead of writing
# the user table ourselves.
#
# The library already provides:
#
# - id (UUID)
# - email
# - hashed_password
# - is_active
# - is_verified
# - is_superuser
#
# We only add extra fields if our application needs them.
#
# Example:
#
# class User(SQLAlchemyBaseUserTableUUID, Base):
#     full_name = Column(String)
#
# relationship() is used to connect User with other tables.
#
# Example:
#
# posts = relationship(
#     "Post",
#     back_populates="user"
# )
#
# This allows:
#
# user.posts
#
# to return every post uploaded by that user.  
# ================================================================
# ========================= USER MANAGER ==========================
# UserManager customizes how FastAPI Users behaves.
#
# The library already knows how to:
#
# - Register users
# - Login users
# - Reset passwords
# - Verify emails
#
# We inherit from BaseUserManager so we don't have to implement
# these features ourselves.
#
# The callback functions below are automatically called by the
# library after specific events happen.
#
# on_after_register()
#     -> Runs after a user registers.
#
# on_after_forgot_password()
#     -> Runs after a reset token is generated.
#
# on_after_request_verify()
#     -> Runs after a verification token is generated.
#
# We usually use these callbacks for:
#
# - Sending emails
# - Logging
# - Notifications
#
# get_user_manager() is a dependency that provides a UserManager
# instance whenever FastAPI needs one.
# ================================================================
# ===================== AUTHENTICATION SETUP ======================
# BearerTransport
#     Defines HOW the JWT token is sent.
#
# Example:
#
# Authorization: Bearer <JWT_TOKEN>
#
# JWTStrategy
#     Defines HOW JWT tokens are created and verified.
#
# It needs:
# - secret key
# - token lifetime
#
# AuthenticationBackend combines:
#
# BearerTransport
#        +
# JWTStrategy
#
# into one authentication system used by FastAPI Users.
# ================================================================