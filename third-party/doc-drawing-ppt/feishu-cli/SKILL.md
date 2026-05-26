---
name: feishu-cli
description: "Operate Feishu/Lark via feishu-cli. Use this skill whenever the user mentions 飞书文档/云文档/wiki/表格/机器人消息/云空间文件/权限协作者设置, or asks to sync local markdown/files with Feishu. Covers config, doc, wiki, sheet, msg, file, media, and perm modules."
---

# Feishu CLI

## When to use

- 读取或更新飞书文档（`doc`）
- 创建/更新知识库页面（`wiki`）
- 读取或写入电子表格（`sheet`）
- 发送飞书消息（`msg`）
- 管理云空间文件/文件夹（`file`）
- 上传下载素材（`media`）
- 管理协作者权限（`perm`）

## Prerequisites

1. Ensure CLI is installed.
```bash
feishu-cli --version
```

2. If missing, install with fixed release (recommended fallback when GitHub API is restricted).
```bash
# macOS arm64 example
curl -fL --progress-bar \
  -o /tmp/feishu-cli_v1.5.0_darwin-arm64.tar.gz \
  https://github.com/riba2534/feishu-cli/releases/download/v1.5.0/feishu-cli_v1.5.0_darwin-arm64.tar.gz

tar -xzf /tmp/feishu-cli_v1.5.0_darwin-arm64.tar.gz -C /tmp
cp /tmp/feishu-cli /Users/bytedance/.codex/bin/feishu-cli
chmod +x /Users/bytedance/.codex/bin/feishu-cli
```

3. Configure credentials (env vars preferred).
```bash
export FEISHU_APP_ID='cli_xxx'
export FEISHU_APP_SECRET='xxxx'
```

4. Optional: initialize local config file.
```bash
feishu-cli config init
```

5. Validate by running a read/create command, e.g.
```bash
feishu-cli doc create --title "smoke-test"
```
If credentials are missing, CLI will return explicit `缺少 app_id/app_secret` errors.

## URL to token hints

- Doc URL usually contains `/docx/{doc_token}`
- Wiki URL usually contains `/wiki/{wiki_token}`
- Sheet URL usually contains `/sheets/{sheet_token}`

When user provides URL, extract token first, then run command.

## Execution workflow

1. Clarify target object and action.
- Object: `doc` / `wiki` / `sheet` / `msg` / `file` / `media` / `perm`
- Action: `read` / `create` / `update` / `send` / `upload` / `download` / `grant`

2. Choose command template from `references/commands.md`.

3. For write operations, prefer safe sequence.
- Read existing state first when feasible.
- Apply minimal scoped changes.
- Ask user confirmation before bulk overwrite/delete.

4. Execute and return concise result.
- Show command (mask secrets)
- Return key IDs/tokens
- Include next fix if failed

## Output format

- Goal
- Command(s) run
- Result
- Next action (if needed)

## Safety rules

- Never print `FEISHU_APP_SECRET` in logs/responses.
- No destructive or bulk write without explicit user confirmation.
- Keep scope to the exact token/range/chat requested.

## References

- Command templates: `references/commands.md`
