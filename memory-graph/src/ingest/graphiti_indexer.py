"""Indexador que toma observations de engram y las carga en Graphiti.

TODO (siguiente agente):
- Inicializar Graphiti con Neo4j + LLM provider (según env vars via shared.config).
- Por cada observation, llamar `graphiti.add_episode(...)` con:
    - name = title de la observation
    - episode_body = content
    - source_description = "engram:{id}"
    - reference_time = created_at (parse ISO)
- Manejar errores por observation individual sin abortar el batch.
- Loguear progreso (X/N indexadas, Y errores, Z segundos, ~$W estimado).
- Idempotente — si una observation ya fue indexada (por id), skip.
"""


class GraphitiIndexer:
    def index_all(self, source) -> None:
        raise NotImplementedError
