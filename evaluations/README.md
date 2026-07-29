# Evaluaciones

Notas de cada piloto — qué funcionó, qué no, decisiones tomadas.

## Convención de archivos

Un archivo por sesión de evaluación:

```
<fecha>-<piloto>-<numero-sesion>.md
```

Ejemplo:
- `2026-07-28-graphiti-pilot-day-1.md`
- `2026-07-29-graphiti-pilot-day-2.md`
- `2026-08-01-graphiti-pilot-final-decision.md`

## Estructura sugerida de cada archivo

```markdown
# <título de la sesión>

## Fecha
YYYY-MM-DD

## Piloto
graphiti-pilot | code-graph-pilot | mcp-servers | ...

## Objetivo de la sesión
Una línea.

## Setup ejecutado
- Comandos que corriste.
- Servicios levantados.
- Costos incurridos.

## Queries evaluadas
1. Query: "..." → resultado: ✅ útil / ⚠️ ruido / ❌ inútil. Nota.
2. ...

## Findings
- Qué funcionó bien.
- Qué falló.
- Sorpresas.

## Decisión
- ✅ Seguir con el piloto.
- ⚠️ Ajustar y re-probar.
- 🛑 Descartar.

## Próximos pasos
- Lista concreta.
```
