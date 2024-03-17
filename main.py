from fastapi import FastAPI

from src.core.configs import settings
from src.api.v1.api import api_router

app = FastAPI(title="Api Base", 
              description="Api base com autenticação para usar em projetos projetos.",
              version="0.01",
              openapi_url="/modelo.json")
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', reload=True)