from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta,
    comparando a senha em texto puro, informada pelo usuário, e o hash da senha que estára 
    criptografada no banco de dados.

    Args:
        senha (str): senha
        hash_senha (str): hash

    Returns:
        bool: true se houver correspondencia.
    """
    
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Gerar hash de senha em texto.
    
    Args:
        senha (str): senha em texto puro

    Returns:
        str: hash da senha
    """
    
    return CRIPTO.hash(senha)