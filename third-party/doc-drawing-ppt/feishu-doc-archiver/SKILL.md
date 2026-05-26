---
name: feishu-doc-archiver
description: Archive generated knowledge documents to Feishu Drive with deterministic folder routing, automatic category creation, and permission sharing. Use this skill whenever the user asks to create/export/publish a document to Feishu, maintain a knowledge base, classify docs into folders, or set collaborator permissions after document delivery.
---

# Feishu Doc Archiver

## Goal
Archive each delivered document into the Codex-managed Feishu knowledge base, keep folder classification stable, and guarantee the user can edit the result immediately.

## Fixed Targets
- Root folder token: `Nfhif9SN1llrOgdy7PEcDQ6HnUe`
- Root folder URL: `https://bytedance.larkoffice.com/drive/folder/Nfhif9SN1llrOgdy7PEcDQ6HnUe`
- Default collaborator email: `baowenjie.233@bytedance.com`
- Default collaborator permission: `edit`
- Category folder tokens:
  - `accounting tech`: `E6WxfErGtlE6hUdOZk0cx1r4nzg`
  - `ai coding`: `NrHqfv1Y5l49RAdT6hUcjbm6nye`
  - `java`: `MGH7fqUiilyLQidFDBxcIHmnnzh`
  - `spark`: `JM6rfblWvl0YSwd02n8cc6KMnHd`

Read `references/routing-and-permission.md` before first use in a task.

## Workflow
1. Classify the document topic into an existing category if possible.
2. Resolve target folder token from the known folder map.
3. Create a new category folder under the root only when no category fits.
4. Prepare or update the local markdown source.
5. Import markdown to Feishu docx using `feishu-cli doc import`.
6. Move the new doc into the target folder using `feishu-cli file move`.
7. Grant `edit` permission to the default collaborator using `feishu-cli perm add`.
8. If a new category folder was created, also grant `edit` on that folder.
9. Return folder link, doc link, permission result, and one-line classification rationale.

## Category Routing Rules
- Route to `accounting tech` for accounting, management-report accounting, reconciliation, TCC scheduling for accounting, or any document the user describes as `核算技术方案` / `管报核算技术方案`.
- Route to `ai coding` for AI agent/protocol/model/prompt/tooling topics.
- Route to `java` for Java, Spring, JVM, service, unit test, or backend runtime topics.
- Route to `spark` for Spark, Hive SQL, data processing, ETL, or compute topics.
- Create a new category folder for topics that clearly do not fit the three defaults.

If the task is clearly an accounting technical document with a fixed archive expectation, prefer the dedicated `accounting-feishu-doc-publisher` skill because it hardens this route and keeps the output format consistent.

## Command Pattern
Use these command patterns directly:

```bash
feishu-cli doc import <markdown_path> --title "<title>" --output json
feishu-cli file move <doc_token> --target <folder_token> --type docx
feishu-cli perm add <doc_token> --doc-type docx --member-type email --member-id baowenjie.233@bytedance.com --perm edit --notification
```

When creating a new category:

```bash
feishu-cli file mkdir "<category_name>" --parent Nfhif9SN1llrOgdy7PEcDQ6HnUe --output json
feishu-cli perm add <new_folder_token> --doc-type folder --member-type email --member-id baowenjie.233@bytedance.com --perm edit --notification
```

## Failure Handling
- If target folder returns `forbidden`, archive to the root folder and state the fallback clearly.
- If API reports missing scopes, state the exact required scope names and stop after actionable guidance.
- If DNS/network fails in sandbox, rerun the same command with escalated execution.
- Do not silently skip permission granting; report success or failure explicitly.

## Response Template
Use this compact template in Chinese:

- 分类目录: `<folder_name>`
- 文档链接: `<doc_url>`
- 目录链接: `<folder_url>`
- 权限: `baowenjie.233@bytedance.com -> edit (success|failed)`
- 分类依据: `<one sentence>`
- 备注: `<fallback or scope action if any>`
