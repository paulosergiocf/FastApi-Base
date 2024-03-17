from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    """
    Descrição: configurações da aplicação.
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DATABASE"]}'
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = os.environ["JWT_SECRET"]
    ALGORITHM: str = os.environ["ALGORITHM"]
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
        
settings: Settings = Settings()