# AGENTS.md — ews-gis-assets

Public publisher of **Austrian wind-turbine GIS datasets** (GeoJSON + GeoPackage).
A daily GitHub Action downloads upstream sources, content-hashes the frames, and
commits `data/` only when the geometry/attributes actually changed.

Org: `EWS-Consulting-Public`. The repo is **public** — treat every file, commit
message and CI log as world-readable.

## Start here

**Read [`README.md`](README.md).** It is the consumer-facing map: which datasets
exist, the raw GitHub URLs, and how the daily update works. Keep it accurate
when you add or rename a published file.

Two flags before you touch anything, both stated in full in rule `gis-project`:

- **This repo is public.** Client names, `F:\` paths, internal host names and
  private estate details never land here — not in code, not in notebooks, not
  in commit messages.
- **`data/` is machine-written.** Humans and agents do not hand-edit published
  GeoJSON/GPKG; the download scripts + Action own that tree.

## The conventions live in rules, not here

All of them load automatically. This file does not restate them — that
duplication is what drifted `AGENTS.md` and `CLAUDE.md` 141 lines apart in
another repo in this estate.

| Rule | Scope | Covers |
|---|---|---|
| [`gis-project`](.cursor/rules/gis-project.mdc) | always | Public-repo privacy, `data/` ownership, uv-only commands, the two download entry points, committing. **Start here if you need to run anything.** |
| [`gis-python`](.cursor/rules/gis-python.mdc) | `**/*.py` | Simplest correct structure, fail fast, absolute imports, content hashing, docstrings that say *why*. |
| [`agent-config-sync`](.cursor/rules/agent-config-sync.mdc) | `{.claude,.cursor}/**` | `.cursor/` is authored, `.claude/` is generated. Never edit the latter. |

## Layout

```text
src/ews_gis_assets/
  noe.py                 NÖ Atlas wind-turbine download + clean
  austro_control.py      Austro Control ICAO obstacle scrape + parse
  helpers.py             content hashing / "did data change?"
  constants.py           upstream URLs
download_noe_wind_turbines.py   CLI entry for the NÖ dataset
download_austro_control.py      CLI entry for the Austro Control dataset
data/                    published GeoJSON + GPKG + .hash sidecars (CI-owned)
.github/workflows/update.yaml   daily midnight UTC refresh
.cursor/                 authored rules (+ skills when any earn a place)
.claude/                 generated - never edit
scripts/sync_agent_config.py
```

## Estate context (orientation only)

Cross-repo orientation lives in the private `fabien-context` checkout
(`C:\Users\f.farella\AI` / `~/AI`). This public repo must not depend on it at
runtime and must not copy private host/path facts into commits. Python taste
and the agent-config layout follow that estate; dataset specifics live here.
