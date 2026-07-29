# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`mala-pata-ai` is a **project-agnostic tooling folder** — it does not host a product repo. Everything here consumes engram memory and/or indexes code from *other* working repos (SIARC, etc.) to give richer context to the SDD agentic workflow, regardless of which CLI runs it. **This document is read by Claude Code specifically, but the software built in this repo must stay coupled to nothing** — not to Claude Code, not to any single CLI. It's consumed equally by Claude Code, Kimi Code, and Codex via the standard MCP contract (see Architecture below). Nothing in here should ever couple to a specific project's stack/domain either; project-specific rules belong in that project's own CLAUDE.md.

Not a git repository. No dependency manifests exist yet (no `requirements.txt`/`pyproject.toml`) — the codebase is currently a **skeleton**, not a working implementation.

## Current state (read before doing anything)

Everything under `memory-graph/src/` and `memory-graph/scripts/` is a stub: function bodies are `raise NotImplementedError` or `exit 1`, each with a `TODO (siguiente agente)` docstring describing exactly what to build. There is no working code to run, build, lint, or test yet — the first job for an agent picking this up is usually to implement one of these stubs per its TODO comment, not to invent new structure.

Full handoff context and decisions live in engram, topic_key `mala-pata-memory/handoff` (observation #7004) — read it via `mem_search` + `mem_get_observation` before making architectural changes here, since it captures decisions that aren't written into any file yet.

**`memory-graph/` is slated to be renamed to `mala-pata-memory/`** (decided in the handoff, not yet executed). `graphiti-pilot/` is the stale first-draft doc for the same effort — treat `memory-graph/` as the current source of truth and `graphiti-pilot/README.md` as superseded.

## Architecture

Four-phase roadmap (see `README.md` and `docs/arquitectura.md` for the full layer diagram):

1. **Memory graph** (`memory-graph/`, active phase) — turns engram's ~6600+ observations into a temporal knowledge graph (Graphiti + Neo4j) so SDD sub-agents get relational context instead of raw text dumps.
2. **Code graph** (`code-graph-pilot/`, not started) — tree-sitter based structural graph of a working repo's code (callers, imports, blast-radius), to replace ad-hoc grep/read during `sdd-explore`/`sdd-tasks`.
3. **MCP integration** — both graphs are consumed exclusively via MCP tool calls, never direct imports, so sub-agents stay decoupled from the underlying graph implementation.
4. **Refresh automation** — incremental re-indexing on `mem_save`/commit hooks, not yet implemented.

### memory-graph internals

```
memory-graph/
├── docker-compose.yml     # Neo4j 5.x — currently an empty `services: {}` stub
├── .env.example           # config template (Neo4j creds, LLM provider, API keys)
├── src/
│   ├── ingest/            # engram observations → Graphiti graph
│   │   ├── engram_source.py     # pluggable reader over engram (mem_search-based)
│   │   ├── graphiti_indexer.py  # calls graphiti.add_episode() per observation
│   │   └── main.py              # entry point: python -m src.ingest.main
│   ├── mcp_server/        # MCP server exposing the graph
│   │   ├── server.py            # entry point: python -m src.mcp_server.server
│   │   └── tools.py              # memory.search / memory.related / memory.timeline / memory.ingest
│   └── shared/
│       ├── config.py            # centralized env var loading (dataclass Config)
│       └── llm_provider.py      # factory: anthropic/openai/google/ollama for Graphiti extraction
├── scripts/{setup,ingest,health}.sh   # all stubs today — see each file's TODO block
└── docs/{mcp-clients,operations}.md
```

The MCP tool contract (`memory.search`, `memory.related`, `memory.timeline`, `memory.ingest` — see `src/mcp_server/tools.py`) is the **universal frontier**: any CLI (Claude Code, Kimi Code, Codex) consumes the graph the same way. Never let a sub-agent import Graphiti/Neo4j directly — always through this MCP layer, so the backend is swappable without touching agent code.

## Hard constraints (from the handoff — do not skip)

- **Never run the ingest (`scripts/ingest.sh` / `graphiti.add_episode`) without explicit user OK.** It makes real LLM API calls (~$7 USD to index the current observation set). List cost before proposing to run it.
- **Never install dependencies without first listing what and their cost/footprint** (disk, API cost) and getting confirmation.
- **Stay CLI-agnostic.** The user explicitly wants this usable from Claude Code, Kimi Code, and Codex — don't hardcode Claude-specific assumptions into `src/` or the MCP contract.
- Config/secrets: `.env` (from `.env.example`) holds real API keys — never read/print/commit it.

## Conventions inherited from the mala-pata ecosystem

These apply to any commit, branch, or script in this repo (source: `~/.claude/commands/mala-pata-loop-perfiles/_base.md`):

- Conventional Commits (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `build`, `ci`, `style`); **no `Co-Authored-By: Claude`** or similar AI-attribution trailers.
- Never `git push` directly to `main`/`master` — always via PR.
- No `git stash` mid-flow, no `--no-verify`/`--no-gpg-sign`, no amending published commits.
- In code: paths relative to the workspace root. When talking to the user: paths relative to the repo, not absolute filesystem paths.
- Don't batch tool calls that aren't actually independent.

## Working style expected here

- **One pilot/phase at a time** — Graphiti (phase 1) is being built now; code-graph (phase 2) is intentionally not started.
- **Reversible by design** — each pilot folder documents its own cleanup (see `graphiti-pilot/README.md`'s Cleanup section as the pattern to follow); if a pilot is abandoned, remove it completely, no dead residue.
- Evaluation notes for each pilot go in `evaluations/`, one file per session, named `<date>-<pilot>-<session-number>.md` (see `evaluations/README.md` for the exact template).
