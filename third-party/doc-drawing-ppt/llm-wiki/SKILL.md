---
name: llm-wiki
description: Maintain a personal LLM-wiki in Markdown. Use when the user asks to initialize, ingest, query, lint, save, explore, or otherwise maintain an LLM-wiki / llm wiki / personal agent-readable wiki. If the target project is not initialized, initialize it first.
---

# LLM Wiki

Use this skill to maintain a Markdown-first personal LLM-wiki for both humans and agents.

## First Step: Detect Or Init

From the target project root, check for:

- `wikis/index.md`
- `wikis/CLAUDE.md`
- `wikis/commands.md`

If any are missing, initialize before doing the requested operation.

Preferred init:

```bash
python3 skills/llm-wiki/scripts/init_llm_wiki.py .
```

If this skill is installed outside the project, resolve the script relative to this `SKILL.md` folder. If the script is unavailable, manually create the same minimal structure:

- `AGENTS.md`
- `README.md`
- `wikis/index.md`
- `wikis/CLAUDE.md`
- `wikis/commands.md`
- `wikis/sources/CLAUDE.md`
- `wikis/craft/CLAUDE.md`
- domain indexes for `ideas/`, `qa/`, `learning/`, `reflections/`
- `wikis/todo.md`
- `wikis/logs/<yyyy-mm>.md`

Do not overwrite existing wiki files during init unless the user explicitly asks.

## Command Routing

Support these command-shaped requests even if there is no real CLI:

- `/wiki init`: initialize the wiki if missing.
- `/wiki ingest <source>`: source to durable wiki entities.
- `/wiki query <question>`: answer from the local wiki first.
- `/wiki lint`: inspect and optionally fix wiki health.
- `/wiki save <summary>`: save reusable knowledge from the current conversation.
- `/wiki explore <topic>`: research a topic, then ingest only useful sources.

Before any route, read `wikis/index.md`, `wikis/CLAUDE.md`, and `wikis/commands.md` after init.

## `/wiki ingest <source>`

Use for URLs, files, docs, repo notes, papers, videos, or conversations.

Required flow:

1. Save or reference raw material under `wikis/sources/`.
2. Create or update a source note with summary, rating, key claims, caveats, agent inference, derived entities, and follow-ups.
3. Extract durable entities into `tech/`, `craft/`, `qa/`, `writing/`, `learning/`, or `reflections/`.
4. Add `[[wikilink]]` references between source and entities.
5. Update `wikis/index.md` when a new important entry point appears.
6. Append the operation to the monthly log.

Quality gate:

- Every source has `source_url` or a local source path.
- At least one durable entity is created, or the final answer explains why extraction was skipped.
- Source-backed facts and agent inference are clearly separated.
- New or changed entities have frontmatter.
- Do not write secrets, tokens, cookies, private keys, or credentials.

## `/wiki query <question>`

Required flow:

1. Read `wikis/index.md`.
2. Identify relevant domains and read their nearest `CLAUDE.md` files.
3. Read the smallest useful set of entities.
4. Answer with local-file evidence when the wiki is used.
5. If the answer becomes durable knowledge, offer to `/wiki save` it.

If relevant local wiki entries exist, do not answer only from model memory.

## `/wiki lint`

Check:

- missing frontmatter
- broken `[[wikilink]]`
- orphan pages
- duplicate concepts
- source notes without derived entities
- stale todos
- stale high-confidence practices
- unresolved contradictions or caveats
- possible credential leakage
- index entries pointing to missing files

Apply safe formatting and link fixes directly. For ambiguous merges, report the decision instead of guessing.

## `/wiki save <summary>`

Route reusable conversation knowledge:

- reusable answer -> `wikis/qa/`
- repeated engineering judgment -> `wikis/craft/practices/`
- explicit user idea -> `wikis/ideas/`
- durable personal principle -> `wikis/reflections/principles.md`

Important: do not write to `wikis/ideas/` unless the user explicitly provided the idea.

## `/wiki explore <topic>`

1. Query the existing wiki first.
2. If current information matters, browse or inspect primary sources.
3. Ingest only sources that pass relevance and quality checks.
4. Create or update synthesis entities.
5. Record open questions and follow-ups.

## L1 / L2 Rule

- L1 files are always-read operation surfaces: `AGENTS.md`, `wikis/index.md`, `wikis/CLAUDE.md`, `wikis/commands.md`.
- L2 files are domain entries read on demand.

Put rules in L1 only when future agents would likely make a bad edit without them. Put background knowledge in L2.

