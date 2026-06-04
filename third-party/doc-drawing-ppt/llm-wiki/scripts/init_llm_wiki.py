#!/usr/bin/env python3
"""Initialize a minimal Markdown-first LLM-wiki without overwriting files."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


TODAY = date.today().isoformat()
MONTH = TODAY[:7]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def init(root: Path) -> list[Path]:
    root = root.resolve()
    created: list[Path] = []

    files = {
        root / "README.md": f"""# LLM Wiki

This repository is a personal LLM-wiki workspace: a Markdown-first knowledge base designed for both human reading and agent use.

Start from `wikis/index.md`. Maintain it with `/wiki ingest`, `/wiki query`, `/wiki lint`, `/wiki save`, and `/wiki explore`.
""",
        root / "AGENTS.md": """# Project Agent Rules

This project is a personal LLM-wiki. Before answering or editing wiki content, read `wikis/index.md`, `wikis/CLAUDE.md`, and `wikis/commands.md`.

- Prefer Markdown files and `[[wikilink]]`.
- Treat `wikis/sources/` as read-only after ingest except metadata fixes.
- Do not write user ideas into `wikis/ideas/` unless the user explicitly provides them.
- Separate source-backed facts from agent inference.
- Log material changes in `wikis/logs/`.
""",
        root / "wikis" / "index.md": """# LLM Wiki

Start here, then load the relevant domain or entity.

## Entry Points

- [[commands]]: command-shaped workflows
- [[todo]]: loose capture and follow-up queue

## Domain Map

- `sources/articles/`: external article source notes
- `tech/`: technical concepts, repos, tools, and model/agent ideas
- `craft/practices/`: engineering and agent-use practices
- `writing/`: writing pipeline
- `ideas/`: user-owned idea pools
- `qa/`: durable Q&A
- `learning/`: study plans and notes
- `reflections/`: principles
""",
        root / "wikis" / "CLAUDE.md": """# LLM Wiki Schema

Default agent entry point for this wiki.

## Principles

- Markdown is the product.
- Work is done at write time: summarize, cross-link, flag contradictions, and preserve open questions.
- `sources/` stores raw material. Distilled knowledge belongs in domain entities.
- `ideas/` is user-owned. AI should not invent entries there.

## Workflows

See [[commands]].

## Entity Frontmatter

```yaml
---
type: concept
title:
status: draft
created:
updated:
source:
tags: []
links: []
---
```
""",
        root / "wikis" / "commands.md": """# Wiki Commands

## `/wiki ingest <source>`

Save or reference the source, create a source note, extract durable entities, add `[[wikilink]]`, update the index when needed, and log the operation.

Quality gate: source path or URL exists; source-backed facts and inference are separated; new entities have frontmatter; no secrets are written.

## `/wiki query <question>`

Read `wikis/index.md`, relevant domain rules, and the smallest useful entity set before answering.

## `/wiki lint`

Check missing frontmatter, broken links, orphan pages, duplicates, stale todos, unresolved caveats, credential leakage, and index entries pointing to missing files.

## `/wiki save <summary>`

Save reusable conversation knowledge to `qa/`, `craft/practices/`, `ideas/`, or `reflections/`. Do not write `ideas/` unless the user explicitly provided the idea.

## `/wiki explore <topic>`

Query local wiki first, research current sources if needed, ingest only useful sources, then record synthesis and follow-ups.
""",
        root / "wikis" / "sources" / "CLAUDE.md": """# Sources Domain

`sources/` stores source notes and raw material references. After ingest, source notes should be treated as read-only except for metadata corrections and link repair.
""",
        root / "wikis" / "craft" / "CLAUDE.md": """# Craft Domain

`craft/` stores personal engineering practices and repeatable judgment.

Confidence values: `emerging`, `established`, `validated`.
""",
        root / "wikis" / "ideas" / "writing.md": f"""---
type: idea-pool
title: Writing Ideas
status: active
created: {TODAY}
updated: {TODAY}
tags: [ideas, writing]
---

# Writing Ideas

User-owned writing ideas go here. AI should not invent entries in this file.

## Inbox

No entries yet.
""",
        root / "wikis" / "ideas" / "products.md": f"""---
type: idea-pool
title: Product Ideas
status: active
created: {TODAY}
updated: {TODAY}
tags: [ideas, product]
---

# Product Ideas

User-owned product ideas go here. AI should not invent entries in this file.

## Inbox

No entries yet.
""",
        root / "wikis" / "qa" / "index.md": f"""---
type: index
title: Q&A
status: active
created: {TODAY}
updated: {TODAY}
tags: [qa]
---

# Q&A

Store durable answers from conversations here when they are likely to be reused.
""",
        root / "wikis" / "learning" / "index.md": f"""---
type: index
title: Learning
status: active
created: {TODAY}
updated: {TODAY}
tags: [learning]
---

# Learning

Use this area for study paths, book notes, algorithms, and structured learning records.
""",
        root / "wikis" / "reflections" / "principles.md": f"""---
type: principles
title: Principles
status: active
created: {TODAY}
updated: {TODAY}
tags: [reflection, principles]
---

# Principles

Record durable personal principles here.
""",
        root / "wikis" / "todo.md": """# Todo

Loose capture for wiki follow-ups. Clean this during lint.

## Inbox

- [ ] Add the first real source through `/wiki ingest`.
""",
        root / "wikis" / "logs" / f"{MONTH}.md": f"""# {MONTH} Log

## {TODAY}

- Initialized the personal LLM-wiki structure.
""",
    }

    directories = [
        root / "wikis" / "sources" / "articles",
        root / "wikis" / "tech" / "llm" / "concepts",
        root / "wikis" / "craft" / "practices",
        root / "wikis" / "writing" / "articles",
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        gitkeep = directory / ".gitkeep"
        if write_if_missing(gitkeep, ""):
            created.append(gitkeep)

    for path, content in files.items():
        if write_if_missing(path, content):
            created.append(path)

    return created


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a minimal LLM-wiki.")
    parser.add_argument("root", nargs="?", default=".", help="Project root to initialize")
    args = parser.parse_args()

    created = init(Path(args.root))
    if created:
        print("created:")
        for path in created:
            print(f"- {path}")
    else:
        print("already initialized; no files created")


if __name__ == "__main__":
    main()

