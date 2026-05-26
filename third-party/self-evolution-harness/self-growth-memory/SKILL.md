---
name: self-growth-memory
description: "Persistent experience-memory loop for engineering work. Use this skill for every non-trivial task (debugging, coding, incident analysis, migration, tool setup): search prior experience before solving, then write a new experience entry after solving, and feed improvements back into other skills."
---

# Self Growth Memory

## When to use

- Any non-trivial task with engineering decisions, troubleshooting, or repeated workflows.
- Any task where past fixes, incident patterns, or command history may help.
- Any task that can improve existing skills after completion.

## Core rule

Do this loop every time:

1. **Before solving**: search the experience library.
2. **After solving**: write a new experience entry.
3. **Skill feedback**: log or apply improvements to relevant skills.

## Required pre-solve checklist

1. Build a short query from user intent and error keywords.
2. Run:
```bash
bash scripts/memory_search.sh "<query>"
```
3. Read matching entries and extract:
- likely root cause patterns
- proven fix strategies
- known pitfalls/regressions
4. If there is no hit, continue normally and mark `no prior hit` in the new entry.

## Required post-solve checklist

1. Capture key facts:
- symptoms/signals
- root cause
- fix
- verification
- residual risk
2. Save a new entry:
```bash
bash scripts/memory_upsert.sh \
  --title "<short title>" \
  --tags "<comma,separated,tags>" \
  --signals "<what failed>" \
  --root-cause "<why>" \
  --fix "<what changed>" \
  --verify "<how verified>" \
  --prevention "<future guardrail>" \
  --related-skills "<skill1,skill2>"
```
3. If a reusable improvement is found for another skill, record it:
```bash
bash scripts/skill_feedback.sh \
  --skill "<skill-name>" \
  --issue "<current limitation>" \
  --proposal "<improvement proposal>" \
  --evidence "<entry filename or link>"
```

## Knowledge library

- `knowledge/index.md`: timeline index of entries
- `knowledge/entries/*.md`: detailed experience notes
- `knowledge/skill_improvement_backlog.md`: pending skill improvements

## Quality bar

- Never store secrets/tokens/keys/passwords.
- Keep entries specific: exact paths, error text, and commands.
- Prefer short actionable lessons over long narrative.
- Each entry must include one prevention rule.

## References

- Workflow details: `references/workflow.md`
