#!/usr/bin/env bash
#
# Pre-commit hook for bumpver
# Updates uv.lock and stages it for commit
#

set -e

echo "🔄 Updating uv.lock..."
uv sync

echo "📝 Staging uv.lock for commit..."
git add uv.lock

echo "✅ uv.lock updated and staged"
