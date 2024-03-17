from pytz import timezone
from typing import Optional, List
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from src.models.usuario_model import UsuarioModel
from src.core.configs import settings
from src.core.security import verificar_senha

from pydantic import EmailStr

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    """
    Args:
        email (EmailStr): email para autenticação
        senha (str): senha em string
        db (AsyncSession): sessão

    Returns:
        Optional[UsuarioModel]: retorna usuario
    """
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        
        if not usuario:
            return None
        
        if not verificar_senha(senha, usuario.senha):
            return None
        
        return usuario
    
def __criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    """
    Doc: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-json-web-token-04#autoid-6
    Args:
        tipo_token (str): tipo do token
        tempo_vida (timedelta): tempo de vida do token
        sub (str): sub

    Returns:
        str: token
    """
    
    payload = {}
    
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_vida
    
    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)
    
    return jwt.encode(payload, settings.JWT_SECRET, settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:
    """
    Doc: https://jwt.io/
    Args:
        sub (str): sub

    Returns:
        str: token
    """
    return __criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )