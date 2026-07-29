"""Definición de las tools MCP que expone el server.

TODO (siguiente agente):
Implementar 4 tools con la firma exacta que consumen sub-agents SDD:

- memory.search(query: str, temporal_window: Optional[str] = None,
                entity_type: Optional[str] = None, limit: int = 10) -> list[Result]
    Devuelve subgrafo relevante para la query.

- memory.related(node_id: str, depth: int = 1) -> list[Node]
    Walk desde un nodo específico N niveles.

- memory.timeline(topic: str) -> list[Fact]
    Hechos ordenados temporalmente relacionados al topic.

- memory.ingest(observation: dict) -> None
    (Fase 2, opcional) hook post-mem_save para refresh incremental.

Cada tool debe tener docstring clara + schema JSON válido para MCP.
"""
