<!-- GENERATED FROM .cursor/rules/public-repo-boundary.mdc BY scripts/sync_agent_config.py.
     Edit the .cursor source, then run: uv run python scripts/sync_agent_config.py -->

**Applies to:** always - this rule is in force for every change.

# This repository is public

`EWS-Consulting-Public/ews-gis-assets` is **world-readable**. The other EWS
repositories you may have worked in are private; the habits that are safe there
are not safe here. Rule `gis-project` § 1 states the boundary in one paragraph
— this rule is the operational half: the list, the check, and the recovery.

**What is published is not only the working tree.** The commit history, every
diff, every commit message, and the *edit history* of every issue and comment
are all public and all permanent. Deleting a line later does not unpublish it.
There is no undo.

## Never write here

- **Host or server names** — internal machines, dev boxes, file servers, any
  `*.local` or intranet hostname.
- **Share layouts and drive paths** — mapped drive letters, UNC paths, DFS
  namespaces, mount points, directory structures on internal storage.
- **Local checkout paths** — any absolute path on a workstation or dev host,
  Windows or POSIX, and anything naming a person's machine or where a
  repository sits on it.
- **Registry identifiers** — a package registry's project id, its account or
  owner, its URL.
- **Client names, site names, commercial detail.** Facts about public Austrian
  open data may live here; evidence from a client project may not.
- **How EWS's private repositories are organised or worked on** — the names of
  private repositories beyond the ones already here, planning board numbers,
  internal file paths, cross-repository issue numbers, or any description of
  how work is coordinated between them.
- **Any credential value.** Not a token, not a password, not a fragment, not an
  example that looks real. Not in a doc, a test fixture, a commit message or an
  issue.

This applies to **files, commit messages, issue and PR text, and code
comments** equally.

## What is fine, and must not be stripped

- The published datasets themselves and everything about their public sources:
  authority names, open-data portals, layer names, licence terms.
- Generic tooling names: `uv`, `ruff`, `pytest`, `nox`, GitHub as a product.
- **The private-repo references already in this tree.** They predate this rule
  and were written deliberately. **Do not add new ones** — and do not silently
  remove the existing ones either. If one should go, that is Fabien's call, not
  a tidy-up, and § *If something internal is already published* is how it goes.

## Before you write

Ask of every new line: **would this tell a stranger something about EWS's
internal infrastructure that they could not already see?** If yes, it does not
go here. It goes in the private hub.

One check that catches the mechanical half, before committing — absolute
paths, UNC shares, intranet hostnames, mount points and long numeric ids:

```bash
git diff --cached | grep -niE '\b[A-Za-z]:\\|\\\\[a-z0-9-]+\\|\.local\b|/mnt/[A-Za-z]\b|\b[0-9]{7,}\b'
```

Add the internal names you are actually working near as a second pass. They
are deliberately not listed in this file: a rule that enumerates the secrets it
protects publishes them itself, and this file is public too.

Neither check is exhaustive — they are a floor, not a proof. Judgment is the
actual mechanism.

## If something internal is already published

**Do not quietly delete it.** Removing the line does not remove it from
history, and a silent fix leaves nobody aware of the exposure. Say what you
found, where, and let Fabien decide. Rewriting public history is his call.

An issue here is published the moment it is opened, and its **edit history
stays readable even after the text is replaced** — so a body template written
for a private repository cannot be un-published by correcting it. That is why
this repository deliberately carries **no long-running internal notes issue**,
and why one must not be created. Internal deploy detail, cross-repo state and
work coordination live in the private hub, never on an issue here.
