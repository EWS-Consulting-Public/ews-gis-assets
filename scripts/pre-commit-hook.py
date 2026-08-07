#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Refresh uv.lock and stage it — runs inside bumpver's pre_commit_hook.

Must finish before bumpver commits, so version files + lock share one commit.
Invoked only via scripts/pre-commit-hook.cmd (cmd/sh polyglot), or:

  uv run --script scripts/pre-commit-hook.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    old = os.environ.get("BUMPVER_OLD_VERSION", "unknown")
    new = os.environ.get("BUMPVER_NEW_VERSION", "unknown")
    print(f"--- Hook: {old} -> {new} ---")

    root = Path(__file__).resolve().parent.parent

    print("Updating uv.lock...")
    sync = subprocess.run(
        ["uv", "sync"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if sync.returncode != 0:
        print(sync.stderr or sync.stdout, file=sys.stderr)
        return 1

    print("Staging uv.lock...")
    add = subprocess.run(
        ["git", "add", "uv.lock"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if add.returncode != 0:
        print(add.stderr or add.stdout, file=sys.stderr)
        return 1

    print("uv.lock staged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
