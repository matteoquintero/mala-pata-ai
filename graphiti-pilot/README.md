# Piloto Fase 1 — Graphiti sobre engram observations

## Objetivo

Convertir tus ~6600 observaciones de engram (decisiones, bugs, patterns, convenciones, kickoffs SDD) en un **knowledge graph temporal** que sub-agents SDD puedan consultar por relaciones, no solo por texto.

Beneficio esperado:
- `sdd-propose` pregunta *"qué convenciones/pitfalls hay sobre paso-3-confirmar"* → recibe **5 observaciones relacionadas con edges tipados**, no 300 chars truncados.
- `sdd-design` pregunta *"cómo abordamos IBC bulk load antes"* → recibe un subgrafo con: decisión + kickoff + bugs previos + tests.
- Reduce el uso de `mem_get_observation` (que hoy trae observations completas de 8-15K cada una).

## Referencia

- [Graphiti (getzep) GitHub](https://github.com/getzep/graphiti)
- [Docs oficiales](https://help.getzep.com/graphiti/)

## Requisitos

1. **Neo4j** (5.x) — Graphiti almacena el grafo en Neo4j.
   - Opción A · Docker local (recomendado para piloto).
   - Opción B · Neo4j AuraDB Free Tier (cloud, 200K nodes / 400K rels max).
2. **Python 3.10+** con `uv` o `pip`.
3. **API key de LLM** para extracción — Anthropic (Claude) o OpenAI.
   - Graphiti usa un LLM para extraer entidades/relaciones de texto libre.
   - Costo esperado del piloto: **~$3-5 USD** para procesar 6600 observations (usando Haiku para extracción).

## Setup — pasos que corrés vos

> 🚧 No corras estos comandos todavía si no querés gastar API tokens en Anthropic/OpenAI. Este piloto tiene costo de LLM externo.

### 1. Neo4j local via Docker

```bash
docker run -d \
  --name mala-pata-neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/mala-pata-2026 \
  -v mala-pata-neo4j-data:/data \
  neo4j:5-community
```

Verificá que arrancó:

```bash
open http://localhost:7474
# Usuario: neo4j · Password: mala-pata-2026
```

### 2. Entorno Python

```bash
cd /Users/matteoquintero/Job/mala-pata-ai/graphiti-pilot
uv venv
source .venv/bin/activate
uv pip install graphiti-core anthropic
```

### 3. Config

Crear archivo `.env` en `graphiti-pilot/`:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=mala-pata-2026
ANTHROPIC_API_KEY=sk-ant-...
GRAPHITI_LLM_MODEL=claude-haiku-4-5-20251001
```

### 4. Exportar observations de engram

Cuando el resto esté listo, el script `scripts/export_engram_to_graphiti.py` (pendiente de escribir) va a:
1. Iterar todas las observations de engram (via `mem_search` iterativo o dump directo del store).
2. Para cada observation: llamar `graphiti.add_episode()` con `content`, `source_description`, `reference_time`.
3. Graphiti extrae entidades + relaciones automáticamente vía LLM.

### 5. Consultar el grafo

```python
from graphiti_core import Graphiti

graphiti = Graphiti(...)
result = await graphiti.search(
    query="paso-3-confirmar componentes reusables",
    center_node_uuid=None,
    limit=10
)
for edge in result.edges:
    print(edge.fact, edge.valid_at)
```

## Evaluación — qué mirar

Después de indexar, prueba estas 5 queries y anotalo en `evaluations/graphiti-pilot-day-1.md`:

1. **Query estructural**: *"decisiones sobre paso-3-confirmar"* — ¿trae los kickoffs relevantes ordenados temporalmente?
2. **Query relacional**: *"componentes creados para revisor-caso"* — ¿trae la lista con `file:line` inferido de las observations?
3. **Query temporal**: *"qué sabíamos sobre CR 75/25 hace 2 semanas"* — ¿respeta la temporalidad?
4. **Query de patterns**: *"convenciones para services HTTP"* — ¿agrupa observations similares?
5. **Query de bugs**: *"bugs de rendering en paso-1 confirmar"* — ¿discrimina bugs vs features?

**Criterios de éxito**:
- ≥3/5 queries devuelven resultado útil (menos ruido que `mem_search` texto).
- El costo de LLM total para la indexación inicial fue ≤$10 USD.
- El grafo cabe en Neo4j Community (nodes ≤ 1M).

**Criterios de fracaso**:
- Extracción de entidades es basura (nombres genéricos, relaciones inventadas).
- Queries devuelven peor contexto que `mem_search` + `mem_get_observation`.
- Costo desproporcionado.

## Cleanup

Si el piloto falla o no vale la pena:

```bash
docker stop mala-pata-neo4j && docker rm mala-pata-neo4j
docker volume rm mala-pata-neo4j-data
rm -rf /Users/matteoquintero/Job/mala-pata-ai/graphiti-pilot/.venv
```

Cero residuos fuera de esta carpeta.

## Estado actual

- 🟡 Documentación y estructura preparadas.
- ⏳ Script de export de engram → Graphiti: pendiente de escribir cuando confirmes que arrancás el piloto (para no ejecutar API calls sin autorización).
- ⏳ Neo4j local: pendiente que vos lo levantes con Docker.
- ⏳ Evaluación: se llena después de correr el piloto.
