# Arquitectura mala-pata-ai

## Objetivo

Dar **contexto estructurado persistente** al workflow agentic sobre Claude Code + engram + SDD, sin acoplar herramientas al repo de trabajo.

## Diagrama de capas

```
┌─────────────────────────────────────────────────────────────────┐
│  Claude Code (orchestrator) + sub-agents SDD                    │
│  ─────────────────────────────────────────────────────────────  │
│  sdd-explore  sdd-propose  sdd-design  sdd-tasks  sdd-verify    │
└─────────────────────────────────────────────────────────────────┘
                              ↓ MCP tool calls
┌─────────────────────────────────────────────────────────────────┐
│  MCP Servers (mcp-servers/)                                     │
│  ─────────────────────────────────────────────────────────────  │
│  memory-graph-mcp        code-graph-mcp                         │
│  (Graphiti-backed)       (tree-sitter-backed)                   │
└─────────────────────────────────────────────────────────────────┘
        ↓                              ↓
┌──────────────────────┐    ┌──────────────────────────────┐
│  Neo4j / Memgraph    │    │  SQLite graph / Memgraph      │
│  ──────────────────  │    │  ──────────────────────────  │
│  Memoria temporal    │    │  Estructura del código        │
│  (engram graph)      │    │  (AST + relaciones)          │
└──────────────────────┘    └──────────────────────────────┘
        ↑                              ↑
        │ ingest                        │ index
┌──────────────────────┐    ┌──────────────────────────────┐
│  engram observations │    │  FRONTEND/ + BACKEND/ code    │
│  (fuente actual)     │    │  (repos de trabajo)          │
└──────────────────────┘    └──────────────────────────────┘
```

## Roles por capa

### Capa 1 · Fuentes (ya existen)

- **engram observations**: memoria persistente ya activa. Cada `mem_save` la enriquece. ~6600 obs actualmente.
- **Repos de código**: FRONTEND (Angular), BACKEND (Django) — vía filesystem local.

### Capa 2 · Grafos derivados (a construir)

- **Memory graph** (Fase 1 · Graphiti): grafo temporal de decisiones/bugs/patterns extraídos de engram. Actualización incremental cada `mem_save`.
- **Code graph** (Fase 2): grafo estructural de símbolos/imports/calls del código. Actualización cada commit o bajo demanda.

### Capa 3 · MCP Servers

- **memory-graph-mcp**: expone `memory.search(query, temporal_window, entity_type)`, `memory.related(node_id, depth)`, `memory.timeline(topic)`.
- **code-graph-mcp**: expone `code.callers(symbol)`, `code.imports(file)`, `code.blast_radius(symbol)`, `code.file_impact(diff)`.

### Capa 4 · Consumo (sub-agents SDD)

Cada sub-agent SDD gana acceso vía MCP tools nuevas:

| Sub-agent | MCP tool nueva | Reemplaza |
|---|---|---|
| `sdd-explore` | `code.callers`, `code.imports` | 3-5 greps + reads |
| `sdd-propose` | `memory.related`, `memory.timeline` | 2-4 `mem_get_observation` |
| `sdd-design` | Ambos | Reads de kickoffs previos + greps de módulos |
| `sdd-tasks` | `code.blast_radius` | Análisis manual de dependencias |
| `sdd-verify` | `code.file_impact` | Búsqueda manual de callers rotos |

## Principios de diseño

1. **Local-first**: todo corre en la máquina del user. Cloud solo para llaves de LLM (Anthropic/OpenAI para extracción de Graphiti).
2. **Un piloto a la vez**: probamos Graphiti primero. Si el ratio esfuerzo/beneficio es bueno, escalamos. Sino, cleanup completo y siguiente candidato.
3. **MCP como frontera**: los sub-agents NO importan librerías Python — todo va via MCP tool calls. Reversible sin tocar los agents.
4. **Sin overhead en el workflow diario**: el ingest de nuevas observations / nuevos commits corre en background (hook post-commit, hook post mem_save). Cero pasos manuales.
5. **Costo transparente**: cada piloto documenta el costo esperado (LLM API + disco) antes de arrancar.

## Roadmap

| Fase | Duración estimada | Costo estimado | Reversible |
|---|---|---|---|
| **1 · Graphiti piloto** | 1-2 días | ~$5 USD LLM + 0 disco | ✅ 1 comando |
| **2 · Code-graph piloto** | 3-5 días | ~$0 (local) + ~500MB disco | ✅ 1 comando |
| **3 · MCP integration** | 2-3 días | ~$0 | ✅ toggle en settings.json |
| **4 · Refresh automation** | 1-2 días | Corre en background, negligible | ✅ desactivable |

## Criterios de éxito global

Después de las 4 fases, medibles:

- **Reducción de reads/greps por SDD**: ≥50% menos operaciones de filesystem.
- **Costo de `sdd-propose`/`sdd-design` bajado**: ≥30% menos tokens (menos re-lectura de observations completas).
- **Calidad del contexto**: la evaluación semanal muestra que las decisiones de propose/design usan referencias más precisas.
- **Overhead operacional**: el usuario no gasta más de 5min/semana manteniendo la infra.

Si algún criterio falla, se documenta en `evaluations/` y se decide continuar o revertir.
