#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INDEX="$ROOT/knowledge/index.md"
ENTRIES_DIR="$ROOT/knowledge/entries"

TITLE=""
TAGS=""
SIGNALS=""
ROOT_CAUSE=""
FIX=""
VERIFY=""
PREVENTION=""
RELATED_SKILLS=""

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/memory_upsert.sh \
    --title "..." \
    --tags "tag1,tag2" \
    --signals "..." \
    --root-cause "..." \
    --fix "..." \
    --verify "..." \
    --prevention "..." \
    --related-skills "skill1,skill2"
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --title) TITLE="${2:-}"; shift 2 ;;
    --tags) TAGS="${2:-}"; shift 2 ;;
    --signals) SIGNALS="${2:-}"; shift 2 ;;
    --root-cause) ROOT_CAUSE="${2:-}"; shift 2 ;;
    --fix) FIX="${2:-}"; shift 2 ;;
    --verify) VERIFY="${2:-}"; shift 2 ;;
    --prevention) PREVENTION="${2:-}"; shift 2 ;;
    --related-skills) RELATED_SKILLS="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$TITLE" || -z "$SIGNALS" || -z "$ROOT_CAUSE" || -z "$FIX" || -z "$VERIFY" || -z "$PREVENTION" ]]; then
  echo "Missing required fields." >&2
  usage
  exit 1
fi

mkdir -p "$ENTRIES_DIR"

TS_HUMAN="$(date '+%Y-%m-%d %H:%M:%S %z')"
TS_FILE="$(date '+%Y-%m-%d_%H%M%S')"
SLUG="$(printf '%s' "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
[[ -z "$SLUG" ]] && SLUG="entry"

ENTRY_FILE="$ENTRIES_DIR/${TS_FILE}_${SLUG}.md"
BASENAME="$(basename "$ENTRY_FILE")"

cat > "$ENTRY_FILE" <<EOF_ENTRY
# $TITLE

- created_at: $TS_HUMAN
- tags: ${TAGS:-none}
- related_skills: ${RELATED_SKILLS:-none}

## Signals
$SIGNALS

## Root Cause
$ROOT_CAUSE

## Fix
$FIX

## Verification
$VERIFY

## Prevention
$PREVENTION
EOF_ENTRY

if [[ ! -f "$INDEX" ]]; then
  cat > "$INDEX" <<'EOF_INDEX'
# Experience Index

EOF_INDEX
fi

echo "- $TS_HUMAN | [$TITLE](entries/$BASENAME) | tags: ${TAGS:-none}" >> "$INDEX"

echo "CREATED: $ENTRY_FILE"
