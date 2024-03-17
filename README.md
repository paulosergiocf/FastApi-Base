# FastApi-Base

Este repositorio tem o objetivo de fornecer uma base miníma ja construida para criação de apis com fast-api.

Funcionalidade:

- [x] Conexão com base de dados assincrona.
- [x] Gerenciamento de usuário.
    - [x] Autenticação com JWT.
- [x] Documentação com Swagger.
- [ ] Testes unitários.
- [ ] Docker File.


## Criação de ambiente virtual

Montagem do ambiente de desenvolvimento.
```sh

    # Criação do ambiente virtual
    python -v venv .venv

    # Ativação do ambiente viertual
    source .venv/bin/activate

    # Instalação de dependencias.
    pip install -r requeriments.txt

```

## Variaveis de ambiente.

Criar arquivo .env na raiz do projeto.

```conf
    DB_USER=postgres
    DB_PASSWORD=SUA_SENHA
    DB_HOST=localhost
    DB_PORT=5432
    DATABASE=postgres # trocar pela sua database caso não utilize o padrão.

    JWT_SECRET= # secretkey pode ser gerada pelo script: configs/gerar_secret.py
    ALGORITHM= # Algoritimo
```


## Base de dados.

Criação de banco de dados postgres no docker para desenvolvimento.

```sh

    docker run --name nome -e "POSTGRES_USERNAME=postgres" -e "POSTGRES_PASSWORD=SUA_SENHA" -p 5432:5432 -d postgres

```


