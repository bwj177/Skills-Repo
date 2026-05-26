# Workflow

## 1) Pre-solve search

Use 2-4 keyword groups:
- system/domain: e.g. spring, tcc, mysql, flyway
- error signature: e.g. BeanCreationException, timeout, access denied
- operation type: e.g. migration, deploy, rollback
- component name: e.g. TosConfig, LarkAppConfig

Search command:
```bash
bash scripts/memory_search.sh "spring tcc BeanCreationException"
```

Decision:
- If matched entries exist: reuse proven approach first.
- If no match: solve from first principles, then create a foundational entry.

## 2) Solve task

Do normal execution and verification.

## 3) Post-solve capture

Create one entry with concrete evidence:
- key logs
- exact files touched
- verification commands

Use command:
```bash
bash scripts/memory_upsert.sh ...
```

## 4) Skill improvement loop

If the solution implies better prompts/workflow for another skill:
- add a backlog item via `scripts/skill_feedback.sh`
- optionally patch that skill immediately if low risk and clearly correct

## 5) Reuse rule

Before each future non-trivial task, run pre-solve search first.
