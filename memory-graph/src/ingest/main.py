"""Entry point del ingest: engram → grafo Graphiti.

Uso:
    python -m src.ingest.main

TODO (siguiente agente):
- Cargar config via shared.config.
- Validar que Neo4j esté vivo (fail-fast si no).
- Construir EngramSource + GraphitiIndexer.
- Ejecutar indexer.index_all(source).
- Reportar resumen final (indexadas, errores, costo estimado).
- Retornar exit code apropiado.
"""


def main() -> int:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
