#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INDEX="$ROOT/knowledge/index.md"
BACKLOG="$ROOT/knowledge/skill_improvement_backlog.md"
ENTRIES_DIR="$ROOT/knowledge/entries"

if [[ $# -lt 1 ]]; then
  echo "Usage: bash scripts/memory_search.sh \"<query>\"" >&2
  exit 1
fi

QUERY="$*"

FILES=()
[[ -f "$INDEX" ]] && FILES+=("$INDEX")
[[ -f "$BACKLOG" ]] && FILES+=("$BACKLOG")
while IFS= read -r file; do
  FILES+=("$file")
done < <(find "$ENTRIES_DIR" -type f -name '*.md' 2>/dev/null | sort)

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "NO_MEMORY_FILES"
  exit 0
fi

echo "QUERY: $QUERY"
if rg -n -i --max-count 200 --no-heading "$QUERY" "${FILES[@]}"; then
  exit 0
fi

TOKENS="$(printf '%s' "$QUERY" | tr -cs '[:alnum:]_-' '\n' | awk 'length>2' | paste -sd'|' -)"
if [[ -n "$TOKENS" ]]; then
  echo "FALLBACK_TOKEN_SEARCH: $TOKENS"
  if rg -n -i --max-count 200 --no-heading "$TOKENS" "${FILES[@]}"; then
    exit 0
  fi
fi

echo "NO_MATCH"
