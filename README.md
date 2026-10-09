# PetshopFood

API backend para gestão de um pet shop, com foco em cadastro de clientes, catálogo de produtos e registro de vendas.

## Visão geral

O PetshopFood foi desenvolvido em Python com FastAPI para oferecer uma API REST simples e organizada para controlar:

- produtos e preços;
- clientes e informações do pet;
- vendas e itens vendidos;
- persistência de dados em PostgreSQL.

O projeto usa SQLModel para modelagem dos dados e Alembic para versionamento do banco de dados.

## Stack tecnológica

- Python 3.14+
- FastAPI
- SQLModel
- PostgreSQL
- Alembic
- Pydantic Settings

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.14.8 ou superior
- uv (recomendado para gerenciamento de dependências)
- PostgreSQL em execução

## Configuração

1. Clone o projeto e acesse a pasta raiz:

```bash
git clone <url-do-repositorio>
cd PetshopFood
```

2. Configure a variável de ambiente do banco em `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/petshop
```

> Ajuste o usuário, senha, host e nome do banco conforme o seu ambiente.

## Instalação

Com `uv`:

```bash
uv sync
```

Se preferir instalar manualmente:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Executando a aplicação

Para iniciar o servidor em modo de desenvolvimento:

```bash
uv run fastapi dev app/main.py
```

Ou usando Uvicorn diretamente:

```bash
uv run uvicorn app.main:app --reload
```

A documentação interativa da API ficará disponível em:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Endpoints atuais

Atualmente a API expõe o endpoint de produtos:

- `GET /products` - retorna uma mensagem de exemplo com a lista de produtos

## Migrações de banco de dados

O projeto usa Alembic para versionar o banco:

```bash
uv run alembic revision --autogenerate -m "initial migration"
uv run alembic upgrade head
```

## Observações

Este projeto está em desenvolvimento inicial, com a base da API e dos modelos já estruturados para expansão futura.

Próximos passos comuns incluem:

- criação de rotas completas para produtos, clientes e vendas;
- validação de dados com schemas específicos;
- autenticação e autorização;
- testes automatizados.

## Licença

Este projeto não possui uma licença definida neste repositório.
