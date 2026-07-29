#!/bin/bash
# health.sh — verifica que Neo4j + MCP server responden.
#
# TODO (siguiente agente):
# 1. Ping a Neo4j (cypher-shell -c "RETURN 1").
# 2. Contar nodes+edges en el grafo (report rápido).
# 3. Ping al MCP server (si está corriendo).
# 4. Verificar que .env tiene todas las vars requeridas.
# 5. Exit code 0 si todo OK, no-cero con diagnóstico si algo falla.

set -euo pipefail

echo "TODO: implementar health check"
exit 1
