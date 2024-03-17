from fastapi import APIRouter
from src.api.v1.endpoints import usuario

api_router = APIRouter()

api_router.include_router(usuario.router, prefix='/usuarios',  tags=['usuarios'])



