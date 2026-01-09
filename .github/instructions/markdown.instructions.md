---
applyTo: "**/*.md"
---

# Markdown Documentation Style

**Write for your users:** Assume readers may be new to Python and the EWS
ecosystem. Prioritize clarity and examples over brevity.

## Formatting Rules

`````markdown
# Use ATX-style headings

## Not underline-style

Use fenced code blocks with language tags:

```python
from ews_wm_base import MeteoParameters
```

## docs/ Folder

Place extended documentation in `docs/` folder.

## GitHub-Friendly Markdown

````markdown
<!-- Use GitHub-style task lists -->

- [ ] Task not done
- [x] Task completed

<!-- Fenced code blocks with language -->

```python
def example():
    ...
```
````
`````

<!-- Tables -->

| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |

<!-- Collapsible sections -->
<details>
<summary>Click to expand</summary>

Hidden content here.

</details>
```

## Prettier Formatting

```bash
# Format markdown files
make md-format                # Uses prettier with project config

# Or format directly with prettier
prettier --print-width 80 --prose-wrap always --write <file>

# Or format specific files
prettier --print-width 80 --prose-wrap always --write README.md docs/**/*.md
```

**Line length:** 80 chars for prose, code examples can be longer for
readability.
