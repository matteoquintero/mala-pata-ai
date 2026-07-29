"""Fuente pluggable que lee observations de engram y las emite para ingest.

TODO (siguiente agente):
- Definir interfaz `EngramSource` con método `iter_observations() -> Iterator[Observation]`.
- Implementar backend que consuma el MCP de engram (mem_search iterativo o dump directo).
- Emitir cada observation con: id, title, content, type, project, scope, created_at, updated_at.
- Manejar paginación / cursor / rate limiting.
- No cachear en memoria todo el set — usar generator para streaming.
"""

from typing import Iterator


class EngramSource:
    """Base class — implementar backends concretos que hereden."""

    def iter_observations(self) -> Iterator[dict]:
        raise NotImplementedError
