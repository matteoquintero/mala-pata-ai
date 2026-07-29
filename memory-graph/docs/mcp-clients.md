# Conectar mala-pata-memory a tu CLI

Guía por CLI para configurar el MCP server de este proyecto como fuente de contexto.

## Claude Code

TODO (siguiente agente): documentar la config en `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "mala-pata-memory": {
      "command": "python",
      "args": ["-m", "src.mcp_server.server"],
      "cwd": "/Users/matteoquintero/Job/mala-pata-ai/memory-graph"
    }
  }
}
```

## Kimi Code

TODO: documentar en `~/.kimi-code/config.toml` — sintaxis MCP de Kimi.

## Codex

TODO: verificar cómo se registran MCP servers en Codex y documentar.

## Verificación

Después de configurar, en cualquiera de los 3 CLIs debería aparecer una tool tipo `memory.search` disponible. Test rápido:

- Prompt: *"usá memory.search para traer decisiones sobre paso-3-confirmar"*.
- Respuesta esperada: subgrafo con edges tipados, no un dump de texto crudo.
