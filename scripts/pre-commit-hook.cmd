#!/usr/bin/env sh
# 2>NUL & goto :windows
# Cross-platform launcher for bumpver pre_commit_hook.
# bumpver does Popen(path) with no interpreter - one file must exec on both OSes.
#   Windows: .cmd is in PATHEXT -> cmd.exe (the "# 2>NUL & goto" line jumps)
#   Linux:  shebang -> sh (skips the goto via the "#" comment, runs exec)
exec uv run --script "$(dirname "$0")/pre-commit-hook.py"
exit
:windows
@echo off
uv run --script "%~dp0pre-commit-hook.py"
exit /b %ERRORLEVEL%
