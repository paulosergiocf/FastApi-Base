import os
from unittest import mock
from pydantic import ValidationError
import pytest

from src.core.configs import Settings


def test_settings_creation():
    """
    Teste para verificar se as configurações são criadas corretamente.
    """
    settings = Settings()
    assert settings.API_V1_STR == '/api/v1'
    assert settings.DB_URL == f'postgresql+asyncpg://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DATABASE"]}'
    assert settings.JWT_SECRET ==  os.environ["JWT_SECRET"]
    assert settings.ALGORITHM ==  os.environ["ALGORITHM"]
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 60 * 24 * 7


def test_settings_case_sensitive():
    """
    Teste para verificar se as configurações são case sensitive.
    """
    with pytest.raises(ValidationError):
        # Forçando uma falha de validação ao definir uma configuração com maiúsculas
        Settings(api_v1_str='/API/v1')

if __name__ == "__main__":
    pytest.main()
