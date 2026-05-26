#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BACKLOG="$ROOT/knowledge/skill_improvement_backlog.md"

SKILL=""
ISSUE=""
PROPOSAL=""
EVIDENCE=""

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/skill_feedback.sh \
    --skill "<skill-name>" \
    --issue "<current issue>" \
    --proposal "<improvement proposal>" \
    --evidence "<entry-file-or-proof>"
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --skill) SKILL="${2:-}"; shift 2 ;;
    --issue) ISSUE="${2:-}"; shift 2 ;;
    --proposal) PROPOSAL="${2:-}"; shift 2 ;;
    --evidence) EVIDENCE="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$SKILL" || -z "$ISSUE" || -z "$PROPOSAL" ]]; then
  echo "Missing required fields." >&2
  usage
  exit 1
fi

if [[ ! -f "$BACKLOG" ]]; then
  cat > "$BACKLOG" <<'EOF_BACKLOG'
# Skill Improvement Backlog

EOF_BACKLOG
fi

TS="$(date '+%Y-%m-%d %H:%M:%S %z')"
{
  echo "- time: $TS"
  echo "  skill: $SKILL"
  echo "  issue: $ISSUE"
  echo "  proposal: $PROPOSAL"
  echo "  evidence: ${EVIDENCE:-none}"
} >> "$BACKLOG"

echo "RECORDED: $SKILL"
