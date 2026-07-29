# mala-pata-ai

Carpeta agnóstica de proyecto — herramientas que dan **contexto persistente y estructurado** al workflow agentic (Claude Code + engram + SDD).

Todo lo que vive acá **NO** pertenece a un repo de trabajo (SIARC, otros). Son herramientas *cross-project* que consumen memorias de engram y/o indexan código de cualquier proyecto para servir mejor a los sub-agents SDD.

## Estructura

```
mala-pata-ai/
├── graphiti-pilot/         # Piloto Fase 1 — engram observations → knowledge graph temporal
├── code-graph-pilot/       # Piloto Fase 2 — código de un repo → grafo estructural (tree-sitter)
├── mcp-servers/            # MCP servers custom que exponen ambos grafos a Claude Code
├── scripts/                # utilidades cross-piloto (export engram, refresh index, etc.)
├── evaluations/            # notas de cada piloto: qué funcionó, qué no, decisiones
└── docs/                   # arquitectura general, guías de operación
```

## Roadmap

| Fase | Estado | Objetivo | Beneficio esperado |
|---|---|---|---|
| **1 · Graphiti** | 🟡 setup pendiente | Convertir ~6600 engram observations en un knowledge graph temporal | `sdd-propose` y `sdd-design` reciben context denso sin re-leer briefs |
| **2 · Code-Graph** | ⏳ post-Fase-1 | Grafo estructural de FRONTEND/BACKEND (tree-sitter + Memgraph o similar) | `sdd-explore` y `sdd-tasks` responden queries de blast-radius sin grep |
| **3 · MCP integration** | ⏳ post-Fase-2 | MCP server local que expone ambos grafos a Claude Code | Sub-agents consultan via tool call, no via read/grep |
| **4 · Refresh automation** | ⏳ post-Fase-3 | Cron/hooks que re-indexan al commit / al mem_save | Los grafos siempre frescos sin trabajo manual |

## Principios

- **Cero acoplamiento a proyecto específico** — nada de SIARC-only aquí. Si algo es SIARC-specific, va al CLAUDE.md de ese repo.
- **Local-first** — todos los grafos corren en tu máquina. Sin cloud dependency salvo llaves de LLM para extracción.
- **Reversible** — cada piloto tiene su carpeta y su cleanup documentado. Si un piloto no sirve, se elimina completo sin residuos.
- **MCP como contrato** — la forma canónica de consumo desde Claude Code es un MCP server, no imports directos.

## Cómo arrancar

Elegí un piloto y seguí su `README.md`:

- **Graphiti primero** (recomendado): `graphiti-pilot/README.md`.
- Code-Graph después: `code-graph-pilot/README.md` (aún placeholder).

## Estado actual

Fecha de creación: 2026-07-28.

- Estructura inicial creada.
- Pilotos: docs preparadas, código pendiente de arrancar (esperando tu OK para tocar dependencias externas).
