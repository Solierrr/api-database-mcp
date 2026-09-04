# Finalidade do repositório

O `api-mcp` é um servidor MCP (Model Context Protocol) que expõe o Postgres "Negócio" da Solaria como um conjunto de ferramentas consultáveis por agentes de IA, em vez de uma API REST tradicional de endpoints fixos. Construído com o SDK `mcp` sobre Starlette/Uvicorn, ele registra ferramentas Python decoradas com `@mcp.tool()` (hoje, listagem de ofertas de placas solares e busca de técnicos credenciados) que um cliente MCP — como o `ai-assistant` da organização — descobre e invoca dinamicamente durante uma conversa, permitindo que o modelo consulte dados de negócio reais sem que cada consulta precise ser modelada como uma rota HTTP própria. O acesso ao banco é feito por um pool de conexões `psycopg2` isolado em `postgres_client.py`, e todo o tráfego do endpoint `/mcp` passa por um middleware de autenticação simples baseado em API key antes de chegar às ferramentas.

<p>

[![License](https://img.shields.io/github/license/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/blob/main/LICENSE)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/commits)
[![GitHub Issues](https://img.shields.io/github/issues/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/pulls)
[![GitHub Contributors](https://img.shields.io/github/contributors/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/graphs/contributors)
[![Release](https://img.shields.io/github/v/release/Solierrr/api-mcp)](https://github.com/Solierrr/api-mcp/releases)

</p>

<div align="center">

<p>
  <a href="https://github.com/syvixor/skills-icons">
    <img src="https://skills.syvixor.com/api/icons?i=python,postgres,docker,github" height="48" alt="Stack do api-mcp">
  </a>
</p>

<p>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-2A9D8F?logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

</p>

</div>

## O que é MCP e por que este servidor existe

- **Model Context Protocol (MCP)**, um protocolo aberto que padroniza como um modelo de linguagem descobre e chama ferramentas externas, em vez de cada integração exigir um contrato HTTP customizado negociado manualmente com o cliente.
- **Ferramentas em vez de endpoints**, cada função decorada com `@mcp.tool()` em `server.py` vira uma capacidade que o agente de IA pode invocar sob demanda, com o schema de entrada e saída inferido a partir da assinatura Python e do docstring da função.
- **Fonte de dados de negócio**, o `api-mcp` conecta diretamente no Postgres "Negócio" (ofertas de fornecedores, técnicos credenciados) para que o `ai-assistant` responda perguntas de negócio com dados reais e atualizados, sem duplicar essa lógica de acesso em cada serviço consumidor.
- **Superfície de ataque reduzida**, como o servidor só expõe leitura via ferramentas específicas (nunca SQL arbitrário vindo do cliente), o raio de exposição do banco fica limitado às consultas que o próprio repositório define.

## Aprofunde-se no Projeto!

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [RUNNING.md](./RUNNING.md)
- {a confirmar: link do arquivo de deployment, caso este repositório siga o padrão de `docs-warehouse/.github/DEPLOYMENT.md`}

## Contribuindo

- [CONTRIBUTING.md](./.github/CONTRIBUTING.md), convenções de commit, branch e Pull Request.
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md), código de conduta do projeto. {a confirmar: arquivo ainda não existe na raiz deste repositório}
- [SECURITY.md](./SECURITY.md), como reportar vulnerabilidades de segurança. {a confirmar: arquivo ainda não existe na raiz deste repositório}
