# Operaciones — mala-pata-memory

Referencia rápida para mantener el servicio corriendo.

## Refresh manual del grafo

TODO (siguiente agente): documentar cuándo/cómo correr `./scripts/ingest.sh`. Recomendación: batch semanal + cuando se agreguen ≥50 observations nuevas.

## Backup del grafo

TODO: documentar cómo hacer `docker exec` + `neo4j-admin dump` para backup del grafo, y cómo restaurar.

## Troubleshooting

TODO: llenar con problemas comunes que aparezcan durante los primeros usos:
- Neo4j no arranca.
- Ingest falla a mitad de camino.
- MCP server no responde.
- Cambio de LLM provider.
- Cambio de API key.

## Métricas a monitorear

- Nodos + edges totales en Neo4j.
- Últimas observations indexadas (timestamp).
- Costo acumulado del LLM provider.
- Latencia promedio de `memory.search`.

## Migración a otra máquina

TODO: documentar los pasos:
1. Copiar `.env`.
2. Backup del volumen Neo4j.
3. Reinstalar deps en la nueva máquina.
4. Restore del volumen.
