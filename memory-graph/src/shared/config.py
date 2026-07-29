"""Carga y valida env vars centralizado.

TODO (siguiente agente):
- Cargar .env con python-dotenv.
- Definir dataclass Config con todos los campos (Neo4j, LLM provider, engram source, MCP).
- Validar en tiempo de carga (fail-fast si falta algo requerido).
- Exportar `get_config()` singleton.
"""

from dataclasses import dataclass


@dataclass
class Config:
    """Configuración runtime — completar campos según .env.example."""
    pass


def get_config() -> Config:
    raise NotImplementedError
