#!/bin/bash
# setup.sh — levanta Neo4j (docker) + Python venv + verifica conectividad.
#
# TODO (siguiente agente):
# 1. Verificar Docker está corriendo.
# 2. `docker compose up -d neo4j` — levantar Neo4j.
# 3. Esperar healthcheck (cypher-shell responde).
# 4. Crear/activar Python venv en .venv/.
# 5. Instalar dependencias: pip install graphiti-core anthropic mcp python-dotenv.
# 6. Verificar .env existe (sino, copiar de .env.example y avisar).
# 7. Correr smoke test: conectar a Neo4j + validar env vars.
# 8. Reportar OK o error claro.

set -euo pipefail

echo "TODO: implementar setup"
exit 1
