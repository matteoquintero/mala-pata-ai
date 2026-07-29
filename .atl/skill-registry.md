# Skill Registry

**Delegator use only.** Any agent that launches sub-agents reads this registry to resolve compact rules, then injects them directly into sub-agent prompts. Sub-agents do NOT read this registry or individual SKILL.md files.

See `_shared/skill-resolver.md` for the full resolution protocol.

**Scope note (mala-pata-ai specific)**: `~/.claude/skills/` is a large SHARED user-level directory (~130 skills) spanning many unrelated domains (marketing, SEO, copywriting, CRO, growth) used across this user's other projects. `mala-pata-ai` is a narrow Python/MCP/knowledge-graph tooling repo. To keep this registry useful without burning budget on irrelevant domains, **Compact Rules were generated only for skills relevant to this project's actual stack** (Python backend architecture, MCP tool design, agent memory/RAG systems, git/PR conventions). All other skills are still listed in the trigger table below for discoverability — if a future change in this project needs one of them, read its SKILL.md directly and add compact rules here.

No project-level skill directories exist yet (`.claude/skills/`, `.gemini/skills/`, `.agent/skills/`, `skills/` are all absent in this repo).

## User Skills (relevant subset — full compact rules generated)

| Trigger | Skill | Path |
|---------|-------|------|
| Designing systems, reviewing code structure, layers/boundaries/dependency direction | clean-architecture | ~/.claude/skills/clean-architecture/SKILL.md |
| DDD, Hexagonal, ports/adapters, aggregates, repositories, bounded contexts, backend structure | clean-ddd-hexagonal | ~/.claude/skills/clean-ddd-hexagonal/SKILL.md |
| Writing/refactoring any code, architecture, code review, TDD | solid | ~/.claude/skills/solid/SKILL.md |
| Applying/choosing/reviewing a GoF design pattern | design-patterns | ~/.claude/skills/design-patterns/SKILL.md |
| Worked code examples for GoF patterns | design-patterns-examples | ~/.claude/skills/design-patterns-examples/SKILL.md |
| Decision rules, checklists, error prevention, forcing functions | heuristics-and-checklists | ~/.claude/skills/heuristics-and-checklists/SKILL.md |
| Creating a pull request / preparing for review | branch-pr | ~/.claude/skills/branch-pr/SKILL.md |
| Creating a GitHub issue / bug report / feature request | issue-creation | ~/.claude/skills/issue-creation/SKILL.md |
| Implementing agent memory, temporal knowledge graphs, choosing memory framework (Mem0/Zep-Graphiti/Letta/Cognee) | memory-systems | ~/.claude/skills/memory-systems/SKILL.md |
| Building RAG systems, vector DBs, semantic/hybrid search | rag-architect | ~/.claude/skills/rag-architect/SKILL.md |
| Combining vector + keyword search (fusion methods) | hybrid-search-implementation | ~/.claude/skills/hybrid-search-implementation/SKILL.md |
| Designing multi-agent systems, sub-agent handoffs, context isolation | multi-agent-patterns | ~/.claude/skills/multi-agent-patterns/SKILL.md |
| Designing agent/MCP tools, tool descriptions, tool consolidation | tool-design | ~/.claude/skills/tool-design/SKILL.md |
| Designing LLM apps, RAG pipelines, agent architectures, LLMOps | llm-app-patterns | ~/.claude/skills/llm-app-patterns/SKILL.md |
| Library/API/framework docs, setup/config questions | context7-mcp | ~/.claude/skills/context7-mcp/SKILL.md |
| Reducing token costs, context budgeting, compaction/masking | context-optimization | ~/.claude/skills/context-optimization/SKILL.md |
| System design / architecture decomposition workflow | software-architect (ctx:architect) | ~/.claude/skills/software-architect/SKILL.md |
| LLM feature development, RAG optimization, multi-provider LLM integration | ai-engineer | ~/.claude/skills/ai-engineer/SKILL.md |

## User Skills (listed only — not project-relevant today, no compact rules generated)

| Skill | Path | Domain |
|-------|------|--------|
| ab-test-setup, ad-creative, advanced-evaluation, ai-seo, analytics-tracking, bdi-mental-states, churn-prevention, cold-email, competitor-alternatives, content-strategy, copy-editing, copywriting, create-image-explain, customer-research, email-sequence, evolutionary-metric-ranking, ffmpeg-analyse-video, form-cro, free-tool-strategy, frontend-design, judgment-day, launch-strategy, lead-magnets, marketing-ideas, marketing-psychology, music-downloader, notebooklm, obsidian-bases, obsidian-cli, obsidian-markdown, onboarding-cro, page-cro, paid-ads, paywall-upgrade-cro, popup-cro, pricing-strategy, product-marketing-context, programmatic-seo, prompt-engineering-patterns, recursos-sentencias, referral-program, revops, sales-enablement, schema-markup, seo* (all seo-* variants), signup-flow-cro, simple-prompts, site-architecture, social-content, spotify-api | ~/.claude/skills/{name}/SKILL.md | Marketing/growth/SEO/CRO/misc — not applicable to this backend tooling repo |
| database-design, database-schema-design | ~/.claude/skills/{name}/SKILL.md | SQL/Postgres/Mongo schema design — this project uses Neo4j (graph), not relational; re-evaluate if a relational store is ever added |
| go-testing | ~/.claude/skills/go-testing/SKILL.md | Go-specific — no Go in this project |
| hosted-agents | ~/.claude/skills/hosted-agents/SKILL.md | Sandboxed/hosted agent infra — not this project's architecture (MCP server, not a hosted-agent platform) |
| filesystem-context, context-fundamentals, context-degradation, context-compression | ~/.claude/skills/{name}/SKILL.md | Context-engineering family — tangential to this project's SDD-context goal; read on demand if context/summarization work is tasked |
| skill-creator, evaluation, heuristic-evaluation, impeccable, json-canvas, tool-design (see relevant), rag-retrieval | ~/.claude/skills/{name}/SKILL.md | Meta / evaluation tooling — read on demand |
| project-development | ~/.claude/skills/project-development/SKILL.md | Generic dev workflow — read on demand |

## Compact Rules

Pre-digested rules per skill. Delegators copy matching blocks into sub-agent prompts as `## Project Standards (auto-resolved)`.

### clean-architecture
- Dependency Direction is CRITICAL: source dependencies point inward only; domain/entities never import infrastructure or framework code
- Interfaces belong to the client (caller), not the implementer — define ports where they're consumed
- Use simple data structures (DTOs) across layer boundaries, not framework-coupled objects
- Entities contain only enterprise business rules, encapsulate invariants, are rich (not anemic), and must not know how they're persisted
- Each use case has one reason to change; declare dependencies explicitly (constructor injection); no presentation logic in use cases
- Structure should scream the domain, not the framework (screaming architecture)
- Keep ORM/web-framework usage confined to infrastructure/interface layers — domain layer has zero framework dependencies
- Tests are part of the architecture — design for testability, test each layer in isolation

### clean-ddd-hexagonal
- Dependency rule: Infrastructure → Application → Domain (never reverse). Validate with: "can this run with no UI/DB?"
- Skip full DDD/hexagonal ceremony for simple CRUD, prototypes, or solo/small-team throwaway code — start simple, evolve only when domain complexity demands it
- One repository PER AGGREGATE (not per entity/table); one aggregate per transaction; cross-aggregate consistency via domain events
- Entity = identity-based equality; Value Object = value-based equality, immutable, no setters
- Anti-patterns to avoid: anemic domain model, repository-per-entity, domain importing DB/HTTP libs, controllers calling repositories directly (must go through application layer), premature CQRS
- Directory layout: domain/{aggregate}/{entity,value_objects,events,repository,services}, application/{use-case}/{command,handler,port}, infrastructure/{persistence,messaging,http,config/di}
- Implementation order: model domain first (no infra) → define ports → implement use cases → adapters last

### solid
- TDD is non-negotiable: RED (failing test) → GREEN (simplest code to pass) → REFACTOR (design happens here, not during initial coding)
- Apply SRP/OCP/LSP/ISP/DIP to every class/module/function — ask "one reason to change?", "extend without modifying?", etc.
- Wrap domain primitives in Value Objects (UserId, Email, Money) — never pass raw strings/numbers for domain concepts
- Naming priority: consistency > understandability (domain language) > specificity > brevity > searchability
- Early returns over `else`; avoid `Object`/map key checks via `in` operator (prototype pollution risk) — use `Object.hasOwn`
- YAGNI/KISS always; DRY only after Rule of Three (3rd duplication triggers extraction)
- Dependencies point toward domain/high-level policy; infrastructure depends on domain, never the reverse

### design-patterns
- Patterns are named solutions to recurring problems — use pattern vocabulary when naming classes/reviewing code ("this is a Strategy", "extract an Adapter")
- Patterns EMERGE from refactoring toward flexibility — never force a pattern preemptively (YAGNI applies)
- Quick lookup: creating objects decoupled from concrete classes → Factory Method/Abstract Factory/Builder; adding behavior without subclassing → Decorator/Strategy/Visitor; decoupling sender/receiver → Observer/Command/Mediator; simplifying a subsystem → Facade/Adapter
- Red flags needing a pattern: class with multiple reasons to change, duplicated object-creation logic, `instanceof`-driven branching, a feature change touching many classes, a growing god object

### heuristics-and-checklists
- Use a HEURISTIC for one-shot decisions (pick an option), a CHECKLIST for repeatable procedures (sequence of steps) — don't conflate the two
- Prefer forcing functions ("does not proceed until X is true") over soft reminders in any process/checklist you design (this mirrors the SDD base rules' "forcing functions" principle)
- Checklists reduce error rates 60-80% empirically (aviation/surgery/software) — keep them short, ordered, and unambiguous (READ-DO or DO-CONFIRM format)
- Satisficing ("good enough" threshold) beats exhaustive analysis under time pressure — define the threshold explicitly before starting

### branch-pr
- Branch naming: `type/description` matching `^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)\/[a-z0-9._-]+$`
- Conventional Commits regex: `^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9._-]+\))?!?: .+`
- NO `Co-Authored-By` or AI-attribution trailers in commits (matches mala-pata-ai's own CLAUDE.md rule)
- PR body must include: linked issue reference, exactly one `type:*` label, summary bullets, changes table, test plan, contributor checklist
- Never merge without required automated checks passing (issue-linkage check, label check, lint/shellcheck)

### issue-creation
- Blank issues disabled — always use bug-report or feature-request template
- Every new issue auto-gets `status:needs-review`; a maintainer must add `status:approved` before any PR referencing it can open
- Search for duplicate issues before filing a new one
- Questions/discussion → GitHub Discussions, not Issues

### memory-systems
- Default to the SIMPLEST memory layer that meets retrieval needs — reliable retrieval beats tool sophistication (Letta's plain filesystem agent beat Mem0's specialized tools on LoCoMo: 74% vs 68.5%)
- Escalation path: file-system (prototype) → vector store/Mem0 (semantic search, multi-tenant) → Zep/Graphiti (relationship traversal + temporal validity + cross-session synthesis) → Letta/Cognee (full self-introspection)
- Choose Zep/Graphiti specifically when bi-temporal modeling is needed (both event time and ingestion time) — directly relevant to `memory-graph/` which is building exactly this (Graphiti + Neo4j on top of engram observations)
- Memory layers: Working (context only) → Short-term (session file/cache) → Long-term (KV/graph DB) → Entity (identity registry) → Temporal KG (validity intervals, time-travel queries)
- Retrieval strategy matches query shape: semantic (direct facts) degrades on multi-hop; entity-based traversal for "everything about X"; temporal filtering for facts that change; hybrid combines all three for best accuracy
- Run consolidation on schedule/threshold to prevent unbounded graph growth — invalidate, don't discard (temporal queries need history)
- Error recovery order: empty retrieval → widen search; stale results → check valid_until, trigger consolidation; conflicting facts → prefer most recent valid_from, surface low-confidence conflicts; storage failure → queue for retry, never block the agent's response on a memory write

### rag-architect
- MUST: evaluate multiple embedding models on real domain data; implement hybrid search (vector + keyword) for any production system; add metadata filters for multi-tenant/domain retrieval; measure precision@k/recall@k/MRR/NDCG, not just LLM output quality; use reranking before final LLM context; implement idempotent ingestion with deduplication
- MUST NOT: default to 512-token chunks without evaluation; skip metadata enrichment (source/timestamp/section); rely on cosine similarity alone for complex domains; couple the embedding model tightly to application code (keep it swappable — matches this project's "never import Graphiti/Neo4j directly, always through MCP" constraint)
- Design output should always include: architecture diagram (ingest + retrieval), vector-store trade-off table, chunking strategy + rationale, retrieval pipeline (query→results), and an evaluation plan with concrete metrics

### hybrid-search-implementation
- Combine vector similarity + keyword (BM25) search when either alone under-recalls, especially for domain vocabulary or exact-match terms (names, codes)
- Fusion methods: RRF (Reciprocal Rank Fusion, general-purpose default), linear weighted sum (tunable alpha), cross-encoder rerank (highest quality, highest cost), cascade (filter then rerank, most efficient)
- RRF formula: score += weight * 1/(k + rank + 1), k≈60 by default — robust without needing score normalization
- When normalizing for linear combination, min-max normalize each result list independently before combining

### multi-agent-patterns
- Sub-agents exist primarily to ISOLATE CONTEXT, not to anthropomorphize roles — don't create a sub-agent unless it removes noise from a shared context
- Multi-agent systems run ~15x the token cost of single-agent chat — only partition when the parallelization/specialization benefit exceeds this overhead
- Three patterns: Supervisor/orchestrator (centralized control, human oversight, but supervisor becomes bottleneck/telephone-game risk), Peer-to-peer/swarm (flexible, explicit handoffs, no single point of failure but coordination complexity grows), Hierarchical (layered abstraction: strategy→planning→execution)
- Fix the "telephone game" problem (supervisor paraphrasing loses fidelity) with a `forward_message`-style passthrough so sub-agent output reaches the user/caller verbatim when synthesis isn't needed
- Default isolation mechanism: instruction passing (sub-agent gets only what it needs); escalate to file-system/shared-state memory only when genuinely needed; avoid full context delegation unless the subtask requires complete understanding
- Never use simple majority voting across agents — weight by confidence/expertise, and watch for sycophantic convergence (agents agreeing to be agreeable, not because they're right)

### tool-design
- Every tool description is prompt engineering — it must answer: what does it do, when to use it, what inputs (with format examples), what it returns (success + error shapes)
- Consolidate overlapping tools into single comprehensive tools (verb encompasses the full workflow) — directly applicable to this project's 4 MCP tools (`memory.search`, `memory.related`, `memory.timeline`, `memory.ingest`): keep them few, non-overlapping, and each with one unambiguous purpose
- Use fully-qualified MCP tool names (`ServerName:tool_name`) in any prompt/doc that references them, to avoid "tool not found" errors when multiple MCP servers are present
- Error messages must be actionable for the CALLING AGENT: state what went wrong AND how to correct it (corrected format example, missing field name) — never just "failed"
- Keep the tool collection small (10-20 tools); use namespacing (`memory.*`) as the collection grows

### llm-app-patterns
- RAG pipeline stages: Ingest (chunk+embed) → Retrieve (vector/hybrid search) → Generate (LLM + context)
- Recommended default chunking: 512 tokens with 50-token overlap, recursive separators (`["\n\n","\n",". "," "]`) — but always validate against domain data (see rag-architect's "MUST evaluate" rule)
- Vector DB choice depends on scale/hosting: pgvector for existing Postgres infra, Chroma for prototyping, Pinecone/Weaviate for production scale — irrelevant to this project directly since it uses Neo4j as the graph store, but relevant if a companion vector index is ever added
- Hybrid search = weighted RRF merge of semantic + keyword (BM25) results; multi-query retrieval (LLM-generated query variations) improves recall for ambiguous queries

### context7-mcp
- Always resolve the library ID first (`resolve-library-id` with libraryName + the user's full question), then fetch docs (`query-docs`) with that ID — never answer library/API/setup questions from training data alone
- Prefer version-specific library IDs when the user names a version (e.g. "Neo4j 5.x", "graphiti-core X.Y")
- Applies directly to this project when implementing graphiti-core, anthropic SDK, or MCP Python library usage — fetch current docs before writing integration code for any of these three

### context-optimization
- Apply in priority order: KV-cache stability (stable content first, dynamic content last in every prompt) → observation masking (compact stale tool outputs, keep them retrievable) → compaction (summarize at >70% context utilization, never touch the system prompt) → context partitioning (split into sub-agents only when a single context can't hold the problem)
- Directly relevant to this project's stated purpose (feeding graph-based context to SDD sub-agents instead of raw text dumps) — the memory-graph tool is itself an implementation of "observation masking + retrieval" at the ecosystem level
- Trigger-based, not periodic: optimize when utilization crosses explicit thresholds (70% compaction, 80% urgent), not on a fixed schedule

### software-architect (ctx:architect)
- Workflow: Understand (problem/constraints/success criteria) → Research existing solutions (don't build custom before checking mature tools) → Specify (functional/non-functional/constraints) → Decompose (1-3 day tasks, mark independent/sequential/parallel-ready) → Plan
- Always produce a build-vs-buy comparison table (maturity, fit, integration, cost, risk) before committing to a custom implementation — relevant before building custom Graphiti/Neo4j glue code that a library might already provide

### ai-engineer
- Multi-provider LLM integration should go through a factory/client abstraction (e.g. `LLMClientFactory` pattern) so the provider is swappable — matches this project's own `src/shared/llm_provider.py` factory design (anthropic/openai/google/ollama)
- Graceful degradation: an auxiliary AI/RAG service failure must never crash the primary flow — fall back to a safe default and log/report, never raise unhandled
- Enforce explicit cost/token guards (max rounds, max tokens per call) for any agentic/ReAct-style loop built on top of the LLM provider layer
