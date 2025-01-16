from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str
    age: int = Field(..., ge=0)  
    todolist = list[str]

