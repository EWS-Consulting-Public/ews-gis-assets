<!-- GENERATED FROM .cursor/rules/agent-config-sync.mdc BY scripts/sync_agent_config.py.
     Edit the .cursor source, then run: uv run python scripts/sync_agent_config.py -->

**Applies to:** `{.claude`, `.cursor}/**`

Skip this rule if your change does not touch those paths.

# Agent config: `.cursor` is authored, `.claude` is generated

**Author under `.cursor/`. Never edit `.claude/` by hand** — it is overwritten.

```bash
uv run python scripts/sync_agent_config.py            # regenerate .claude/
uv run python scripts/sync_agent_config.py --check    # verify; exit 1 on drift
```

| Source (authored) | Target (generated) |
|---|---|
| `.cursor/rules/<name>.mdc` | `.claude/rules/<name>.md` |
| `.cursor/skills/<x>/**` | `.claude/skills/<x>/**` (byte-for-byte) |

Files under `.claude/` with no `.cursor/` source are **deleted**, so renaming a
rule cannot leave a stale copy loading forever. prek runs `--check`.

## Why generated, not hand-mirrored

The two tools scope rules differently. **Cursor** reads `globs` /
`alwaysApply` and loads a rule only when matching files are open. **Claude
Code** loads every `.claude/rules/*.md` unconditionally — there is no path
scoping. So the trees cannot be byte-identical for rules, and a human mirroring
them by hand will drift.

That is not hypothetical: in `ews-windpro` the hand-mirroring rule drifted until
four rules `AGENTS.md` called always-on had **no Claude counterpart at all**,
leaving two documented hard boundaries absent from every Claude session.

The generator preserves the Cursor scope as an **Applies to** header, so a
path-scoped rule stays self-gating once loaded.

The generator itself is copied from `ews-windpro/scripts/sync_agent_config.py`
on purpose. Port fixes between them rather than diverging — a second
implementation is a second thing that can be subtly wrong.

## Adding or renaming a rule

1. Write the `.mdc` under `.cursor/rules/` with full frontmatter
   (`description`, `globs`, `alwaysApply`).
2. Regenerate.
3. Commit **both** trees — the generated tree is checked in so an agent that
   only sees `.claude/` still gets the rules.
4. Update the rule table in [`AGENTS.md`](../../AGENTS.md).

**Keep the rule set small.** Rules load every session; a large set of narrow
rules is what drifted in `ews-windpro` before the generator existed.

## Writing skills that survive the copy

Skills are copied **byte-for-byte**, so a relative link resolves from whichever
tree the reader is in.

- Links up to repo-root content are fine — `.cursor/skills/x/` and
  `.claude/skills/x/` sit at the same depth, so `../../../Architecture.md`
  resolves in both.
- **Never link into `.cursor/` itself** from a skill: `../../rules/…` resolves
  to `.claude/rules/…` in the copy, which holds a *different* file name
  (`.md`, not `.mdc`). Name such a path in backticks instead of linking it.
- **The `description:` frontmatter is the dispatch mechanism, not a summary.**
  An agent picks a skill from its name and description alone; the body is read
  only after it is picked. A description that has drifted from what the skill
  does means the skill **silently never fires**, and nothing errors. Update it
  in the same edit as the behaviour.
