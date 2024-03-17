from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine

from src.core.configs import settings

"""Criar Engine"""
engine: AsyncEngine = create_async_engine(settings.DB_URL)

"""Descrição: Criar sessão."""
Session: AsyncSession = sessionmaker(
    
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

