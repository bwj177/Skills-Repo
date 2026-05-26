# feishu-cli Command Templates (v1.5.0 aligned)

Use these as base commands. Replace placeholders like `<doc_token>` / `<chat_id>` / `<sheet_token>` before execution.

## 1) Config & Credential Check

```bash
# show CLI version
feishu-cli --version

# initialize local config file (~/.feishu-cli/config.yaml)
feishu-cli config init

# environment variables preferred
export FEISHU_APP_ID='cli_xxx'
export FEISHU_APP_SECRET='xxxx'

# simple auth-required smoke test
feishu-cli doc create --title "smoke-test"
```

## 2) Doc (飞书文档)

```bash
# create doc
feishu-cli doc create --title "My Document"

# get doc info
feishu-cli doc get <doc_token>

# read all blocks (JSON)
feishu-cli doc blocks <doc_token>

# import markdown to new/existing doc
feishu-cli doc import README.md --title "导入文档"
feishu-cli doc import README.md --document-id <doc_token>

# export doc markdown (token or full URL)
feishu-cli doc export <doc_token> --output doc.md
feishu-cli doc export "https://xxx.feishu.cn/docx/<doc_token>" --output doc.md
```

## 3) Wiki (知识库)

```bash
# list wiki spaces
feishu-cli wiki spaces

# list nodes in a space
feishu-cli wiki nodes <space_id>

# create node in space
feishu-cli wiki create --space-id <space_id> --title "Wiki Page"

# get / update / delete node
feishu-cli wiki get <node_token>
feishu-cli wiki update <node_token> --title "新标题"
feishu-cli wiki delete <node_token>

# export wiki node to markdown
feishu-cli wiki export <node_token> --output wiki.md
```

## 4) Sheet (电子表格)

```bash
# read range
feishu-cli sheet read <sheet_token> "Sheet1!A1:C10"

# write range (JSON 2D array)
feishu-cli sheet write <sheet_token> "Sheet1!A1:B2" \
  --data '[["姓名","年龄"],["张三",25]]'

# list/add/delete worksheet
feishu-cli sheet list-sheets <sheet_token>
feishu-cli sheet add-sheet <sheet_token> --title "Sheet2"
feishu-cli sheet delete-sheet <sheet_token> <sheet_id>
```

## 5) Message (飞书消息)

```bash
# send text
feishu-cli msg send \
  --receive-id-type chat_id \
  --receive-id <chat_id> \
  --text "Hello from feishu-cli"

# send interactive card
feishu-cli msg send \
  --receive-id-type chat_id \
  --receive-id <chat_id> \
  --msg-type interactive \
  --content-file card.json

# search chats
feishu-cli msg search-chats --name "群名关键字"
```

## 6) File (云空间文件)

```bash
# list root / folder
feishu-cli file list
feishu-cli file list <folder_token>

# create folder
feishu-cli file mkdir "新文件夹"
feishu-cli file mkdir "子文件夹" --parent <folder_token>

# move/copy/delete file
feishu-cli file move <file_token> --target <folder_token> --type docx
feishu-cli file copy <file_token> --target <folder_token> --type docx
feishu-cli file delete <file_token> --type docx

# query quota
feishu-cli file quota
```

## 7) Media (素材)

```bash
# upload image/file to doc context
feishu-cli media upload image.png --parent-type docx_image --parent-node <doc_token>
feishu-cli media upload manual.pdf --parent-type docx_file --parent-node <doc_token>

# download by file token
feishu-cli media download <file_token> --output downloaded_file.bin
```

## 8) Permission (协作者权限)

```bash
# grant edit permission
feishu-cli perm add <doc_token> \
  --doc-type docx \
  --member-type email \
  --member-id user@example.com \
  --perm edit

# update to view/full_access
feishu-cli perm update <doc_token> \
  --doc-type docx \
  --member-type email \
  --member-id user@example.com \
  --perm view
```

## 9) Troubleshooting

```bash
feishu-cli --help
feishu-cli doc --help
feishu-cli wiki --help
feishu-cli sheet --help
feishu-cli msg --help
feishu-cli file --help
feishu-cli media --help
feishu-cli perm --help
```

Common issues:

- `缺少 app_id / app_secret`: credentials not configured in env/config
- `403`: app does not have required Open Platform scopes
- `404 token not found`: wrong token type or wrong resource token
- `invalid range`: verify range format `Sheet1!A1:C10` and sheet id
