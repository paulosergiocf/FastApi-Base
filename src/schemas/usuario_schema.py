from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UsuarioSchemaBase(BaseModel):
    id: Optional[int]
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True
    

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
       
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
    