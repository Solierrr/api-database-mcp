"""Servidor MCP que expõe o Postgres 'Negócio'."""

import uvicorn
from mcp.server.mcpserver import MCPServer
from postgres_client import get_cursor
from settings import settings

mcp = MCPServer("solaria-negocio")


@mcp.tool()
def listar_ofertas_de_placas(potencia_minima_wp: float = 0, marca: str = "") -> list[dict]:
    """Lista ofertas de placas solares disponíveis, com fornecedor, preço e
    potência. Filtra por potência mínima em Wp e/ou marca, se informado."""
    with get_cursor() as cur:
        cur.execute(
            """
            SELECT
                comp.trade_name AS fornecedor,
                m.brand AS marca,
                m.model AS modelo,
                m.power_wp AS potencia_wp,
                m.efficiency AS eficiencia_pct,
                o.unit_price AS preco_unitario,
                o.availability AS disponibilidade,
                o.expiration_date AS validade
            FROM offer o
            JOIN supplier s ON s.id = o.fk_supplier
            JOIN company comp ON comp.id = s.fk_company
            JOIN model m ON m.id = o.fk_model
            WHERE s.status = 'ACTIVE'
              AND m.status = 'APPROVED'
              AND m.power_wp >= %(potencia_minima_wp)s
              AND (%(marca)s = '' OR m.brand ILIKE %(marca)s)
            ORDER BY o.unit_price ASC;
            """,
            {"potencia_minima_wp": potencia_minima_wp, "marca": f"%{marca}%" if marca else ""},
        )
        return cur.fetchall()


app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
