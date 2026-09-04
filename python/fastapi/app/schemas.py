from pydantic import BaseModel
from fastapi_users import schemas
import uuid
class postcreate(BaseModel):# specifying the data type of input data
    title: str
    content: str
class postreturn(BaseModel):# specifying the data type of output data
    title: str
    content: str
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass
class UserCreate(schemas.BaseUserCreate):
    pass
class UserUpdate(schemas.BaseUserUpdate):
    pass