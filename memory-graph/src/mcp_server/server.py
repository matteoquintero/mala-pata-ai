"""MCP server para mala-pata-memory — expone el grafo a Claude/Kimi/Codex.

TODO (siguiente agente):
- Usar la librería MCP oficial de Python (mcp).
- Inicializar con transport stdio (por defecto) o HTTP según env.
- Registrar las tools de tools.py.
- Conectar a Neo4j+Graphiti (via shared.config).
- Manejar shutdown limpio.

Uso:
    python -m src.mcp_server.server
"""


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
