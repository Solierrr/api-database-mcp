# api-mcp

Servidor MCP que expõe consultas ao Postgres "Negócio" da plataforma
Solária (fornecedores, ofertas de placas solares, técnicos credenciados)
para o ai-assistant, via protocolo MCP autenticado por API key.

Este repositório **não é dono** do schema do banco "Negócio" — só
consulta. O schema é mantido por outro sistema; uma cópia de referência
fica em `docs/schema_negocio.sql`.

## Rodando localmente

1. `cp .env.example .env` e preencher `DATABASE_URL`/`MCP_API_KEY`
2. `pip install -r requirements.txt`
3. `python server.py`

## Rodando via Docker

```
docker build -t api-mcp .
docker run --env-file .env -p 8001:8001 api-mcp
```

## Tools disponíveis

- `listar_ofertas_de_placas(potencia_minima_wp, marca)` — ofertas ativas
  de placas solares, com preço e fornecedor
- `buscar_tecnicos_credenciados(profissao, cidade)` — técnicos afiliados a
  alguma empresa, com registro profissional

## Testes

```
python -m pytest tests -v
```

Os testes não precisam de Postgres real rodando (tudo mockado) nem de
`.env` (o `tests/conftest.py` já define valores fake pra `Settings`).
