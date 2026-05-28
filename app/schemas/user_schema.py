from pydantic import BaseModel, EmailStr

# Registration schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str