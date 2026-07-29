# memory-graph · mala-pata-memory

Servicio local que convierte las memorias persistentes de engram en un **knowledge graph temporal** consultable vía **MCP**, para alimentar sub-agents SDD con contexto denso y estructurado.

**Producto interno agnóstico de CLI** — consumible desde Claude Code, Kimi Code y Codex mediante MCP.

## Estado

🚧 **Skeleton creado, implementación pendiente.**

Handoff completo del contexto y decisiones en engram: topic_key `mala-pata-memory/handoff`.

## Estructura

```
memory-graph/
├── README.md                   # este archivo
├── docker-compose.yml          # Neo4j + servicios auxiliares
├── .env.example                # template de config (API keys, URIs)
├── src/
│   ├── ingest/                 # engram observations → grafo (Python)
│   ├── mcp_server/             # MCP server que expone el grafo
│   └── shared/                 # config + provider abstraction
├── scripts/                    # setup, ingest, health
└── docs/                       # cómo conectar cada CLI, operations
```

## Setup rápido (cuando esté implementado)

1. Copiar `.env.example` → `.env` y completar con tu API key.
2. `./scripts/setup.sh` — levanta Neo4j + Python venv + verificaciones.
3. `./scripts/ingest.sh` — indexa observations de engram al grafo (costo LLM real).
4. Configurar el MCP server en tu CLI — ver `docs/mcp-clients.md`.

## Próximos pasos

Ver `mala-pata-memory/handoff` en engram (#7004) — lista de tareas concretas para el agente que continúe.
