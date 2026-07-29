# Piloto Fase 2 — Grafo estructural del código

## Objetivo

Construir un **knowledge graph estructural** de un repo (FRONTEND o BACKEND) usando tree-sitter AST parsing. Consultar via MCP para responder queries de tipo:

- "Quién llama a `descargarPdf`?"
- "Qué imports tiene `paso-6-carta.component.ts`?"
- "Blast-radius: si toco el interface `Liquidacion`, qué archivos se afectan?"
- "Dame las 5 funciones más largas del módulo sentencias/."

Beneficio esperado:
- `sdd-explore` y `sdd-tasks` **NO leen archivos raw** — hacen queries al grafo y reciben resultados estructurados.
- `sdd-verify` sabe si el diff afecta símbolos importantes sin correr el linter.

## Estado

⏳ **Pendiente** — arrancar solo después de que Graphiti-pilot esté evaluado y decidido.

## Candidatos a estudiar

| Proyecto | Pro | Contra |
|---|---|---|
| [Code-Graph-RAG](https://code-graph-rag.com/) | 13 lenguajes, MCP nativo | Requiere Memgraph (extra service) |
| [Codebase Expert](https://github.com/darit/codebase-expert) | Liviano, semantic+keyword híbrido | Menos maduro |
| [GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Client-side, sin backend | Limitado por memoria del browser en repos grandes |
| [OpenCode Codebase Index](https://github.com/Helweg/opencode-codebase-index) | Rust + tree-sitter, muy rápido | Solo para OpenCode integration |
| Custom (tree-sitter + SQLite graph) | Control total | Trabajo de mantenimiento propio |

## Decisión pendiente

Elegir 1 candidato después de:
1. Ver los resultados de Graphiti-pilot (aprendizaje sobre indexación + MCP).
2. Confirmar que el grafo del código es una necesidad real (no cubierta ya por Graphiti sobre engram).

## Cuando arranque

Este README se reemplaza por documentación específica del candidato elegido, con estructura similar a `graphiti-pilot/README.md`:
- Requisitos
- Setup
- Config
- Indexado inicial
- Evaluación
- Cleanup
