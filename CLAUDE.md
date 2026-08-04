# CLAUDE.md — ews-gis-assets

@AGENTS.md

Claude Code entrypoint. Shared project instructions live in
[`AGENTS.md`](AGENTS.md) (imported above) — this file adds only what is
Claude-specific.

## Claude-local pointers

- **`.claude/rules/` and `.claude/skills/` are generated** from `.cursor/` and
  are committed. Never edit them by hand — author under `.cursor/`, then
  `uv run python scripts/sync_agent_config.py`. prek runs `--check`.
- Claude Code loads **every** rule under [`.claude/rules/`](.claude/rules/)
  unconditionally, so each carries an **Applies to** header naming the paths it
  is scoped to in Cursor. Skip a rule whose paths your change does not touch.
- Skills: [`.claude/skills/`](.claude/skills/) — byte-for-byte copies of
  `.cursor/skills/` (none yet; add under `.cursor/` when a procedure earns one).
