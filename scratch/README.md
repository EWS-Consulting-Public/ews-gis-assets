# scratch/

Local probes, dumps, and throwaway scripts. **Not part of the published
dataset pipeline.**

- Contents are gitignored (see `.gitignore` here). Only this README and that
  ignore file are tracked.
- Put work under `scratch/<topic>/…` — do **not** dump `_scratch*` files at the
  repo root.
- This is a **public** repo: no client names, `F:\` paths, or internal host
  names. Same privacy rule as everywhere else (`gis-project` §1).

When a probe graduates into a real downloader, move it into
`src/ews_gis_assets/` plus a `download_*.py` entry point — do not promote from
here by renaming in place.
