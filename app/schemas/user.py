from pydantic import BaseModel, EmailStr
from pydantic.config import ConfigDict

# Schema para cadastro de usuário
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Schema para login (sem nome)
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema para retorno de dados públicos
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
