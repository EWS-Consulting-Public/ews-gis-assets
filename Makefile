OS := $(shell uname -s)
NPROCS ?= $(shell nproc)
SHELL := /bin/bash

.DEFAULT_GOAL := format

PROJECT_ROOT := $(abspath .)
DOCS_DIR := $(PROJECT_ROOT)/docs
VENV := $(PROJECT_ROOT)/.venv/
PYTHON := $(VENV)/bin/python
PYTEST := $(VENV)/bin/pytest
UV := uv

EXTRA_ARGS ?=

# PRETTIER_CMD detection: prefer any prettier on PATH, otherwise fall back to `npx prettier` so we don't require a global install.
PRETTIER_CMD ?= $(shell \
if command -v prettier >/dev/null 2>&1; then \
	command -v prettier; \
else \
	echo "npx prettier"; \
fi)
PRECOMMIT_CMD ?= $(shell \
if command -v prek >/dev/null 2>&1; then \
	command -v prek; \
else \
	echo "uvx prek"; \
fi)
PRETTIER_ARGS ?= --ignore-path .prettierignore --print-width 80 --prose-wrap preserve

.PHONY: help
help:
	@echo "Available targets:"
	@echo ""
	@echo "Formatting:"
	@echo "  ruff-format                 Format and lint code with ruff"
	@echo "  md-format                   Format and fix markdown files"
	@echo "  nb-strip-notebooks          Strip notebooks (excluding certain directories)"
	@echo "  notebooks-from-py           Generate .ipynb files from .py notebooks (after clone)"
	@echo "  pre-commit-all-files        Run pre-commit hooks on all files"
	@echo "  format                      Run all formatting targets"
	@echo ""
	@echo "Testing:"
	@echo "  test                        Run tests with UV"
	@echo "  test-coverage               Generate coverage report (HTML + terminal)"
	@echo "  test-failed                 Rerun only failed tests"
	@echo "  test-verbose                Run tests with verbose output"
	@echo "  test-quick                  Fast tests (fail-fast mode)"
	@echo "  test-list                   List all tests without executing"
	@echo ""
	@echo "Build & Release:"
	@echo "  build                       Build wheel for distribution"
	@echo "  release                     Release with bumpver (CalVer)"
	@echo "  release-patch               Same-day patch release"
	@echo ""
	@echo "Utilities:"
	@echo "  setup                       Set up development environment (git filters, pre-commit hooks)"
	@echo "  clean                       Clean up build artifacts and caches"
	@echo "  nox-list                    List all available nox sessions"



# ============================================================================
# Testing targets (via nox)
# ============================================================================

.PHONY: test
test:
	@nox -s test

.PHONY: test-coverage
test-coverage:
	@nox -s pytest_coverage

.PHONY: test-failed
test-failed:
	@nox -s pytest_failed

.PHONY: test-verbose
test-verbose:
	@nox -s pytest_verbose

.PHONY: test-quick
test-quick:
	@nox -s pytest_quick

# List all tests without executing them
.PHONY: test-list
test-list:
	$(PYTEST) --collect-only || true


# ============================================================================
# Build & Release targets (via nox)
# ============================================================================

.PHONY: build
build:
	@nox -s build

.PHONY: release
release:
	@nox -s release

.PHONY: release-patch
release-patch:
	@nox -s release -- patch

.PHONY: nox-list
nox-list:
	@nox -s list


# ============================================================================
# Formatting targets
# ============================================================================

# Format and lint code with ruff
.PHONY: ruff-format
ruff-format:
	@echo "Formatting code with ruff..."
	$(UV) run ruff format $(EXTRA_ARGS)
	@echo "Linting code with ruff..."
	$(UV) run ruff check --fix --show-fixes --unsafe-fixes $(EXTRA_ARGS) || true

# Format and fix markdown files
.PHONY: md-format
md-format:
	@echo "Formatting markdown files..."
	@# Format docs if any markdown files exist (portable find)
	@if [ -d "$(DOCS_DIR)" ] && find "$(DOCS_DIR)" -type f -name '*.md' -print -quit | grep -q .; then \
		find "$(DOCS_DIR)" -type f -name '*.md' -print0 | xargs -0 $(PRETTIER_CMD) $(PRETTIER_ARGS) --write $(EXTRA_ARGS) || true; \
	else \
		echo "No docs markdown files found in $(DOCS_DIR)"; \
	fi
	# Format .github markdown files if any exist (config, instructions, etc.)
	@if [ -d ".github" ] && find ".github" -type f -name '*.md' -print -quit | grep -q .; then \
		find ".github" -type f -name '*.md' -print0 | xargs -0 $(PRETTIER_CMD) $(PRETTIER_ARGS) --write $(EXTRA_ARGS) || true; \
	else \
		echo "No .github markdown files found"; \
	fi
	@# Format README.md if present
	@if [ -f README.md ]; then \
		$(PRETTIER_CMD) $(PRETTIER_ARGS) --write README.md $(EXTRA_ARGS) || true; \
	else \
		echo "No README.md found"; \
	fi

# Strip notebooks (excluding certain directories)
.PHONY: nb-strip-notebooks
nb-strip-notebooks:
	@if ! command -v nbstripout-fast >/dev/null 2>&1; then \
		echo "⚠️  nbstripout-fast not found. Skipping notebook stripping."; \
		echo "   Install it with: uv tool install nbstripout-fast"; \
	else \
		echo "Stripping notebooks (excluding any .venv/ , docs/ , .ipynb_checkpoints/ , and .virtual_documents/ directories)..."; \
		find . \( -type d \( -name '.venv' -o -name 'docs' -o -name '.ipynb_checkpoints' -o -name '.virtual_documents' \) -prune \) -o -type f -name '*.ipynb' -print0 \
		| while IFS= read -r -d '' f; do \
			if nbstripout-fast "$$f" >/dev/null 2>&1; then \
				echo "STRIPPED: $$f"; \
			else \
				echo "FAILED nbstripout: $$f"; \
			fi; \
		done; \
	fi

# Generate .ipynb from .py notebooks (useful after cloning if only .py files are in git)
.PHONY: notebooks-from-py
notebooks-from-py:
	@echo "Converting .py notebooks to .ipynb format..."
	@if ! command -v uvx >/dev/null 2>&1; then \
		echo "❌ uvx not found. Install UV first."; \
		exit 1; \
	fi
	@py_count=$$(find . -type f -name '*.py' \
		\( -path '*/notebooks/*.py' -o -path '*/examples/*.py' -o -path '*/docs/*.py' \) \
		! -path '*/.venv/*' ! -path '*/__pycache__/*' \
		| wc -l); \
	if [ "$$py_count" -eq 0 ]; then \
		echo "No .py notebook files found in notebooks/, examples/, or docs/ directories"; \
	else \
		echo "Found $$py_count .py notebook file(s)"; \
		find . -type f -name '*.py' \
			\( -path '*/notebooks/*.py' -o -path '*/examples/*.py' -o -path '*/docs/*.py' \) \
			! -path '*/.venv/*' ! -path '*/__pycache__/*' \
			-print0 | while IFS= read -r -d '' f; do \
				echo "  Converting: $$f"; \
				uvx jupytext --to ipynb "$$f" || echo "  ⚠️  Failed: $$f"; \
			done; \
		echo "✅ Conversion complete! You can now open notebooks in Jupyter."; \
	fi

.PHONY: pre-commit-all-files
pre-commit-all-files:
	@echo "Running pre-commit hooks..."
	$(PRECOMMIT_CMD) run --all-files

.PHONY: setup
setup:
	@echo "Setting up development environment..."
	$(UV) sync --all-extras
	@if ! command -v nbstripout-fast >/dev/null 2>&1; then \
		echo "❌ nbstripout-fast not found. Install it with: uv tool install nbstripout-fast"; \
		exit 1; \
	else \
		git config filter.jupyter.clean nbstripout-fast; \
		git config filter.jupyter.smudge cat; \
		echo "✅ nbstripout-fast found."; \
	fi
	@if ! command -v prek >/dev/null 2>&1; then \
		echo "❌ prek not found. Install it with: uv tool install prek"; \
		exit 1; \
	else \
		echo "✅ prek found."; \
	fi
	$(PRECOMMIT_CMD) install -f

.PHONY: format
format: ruff-format md-format nb-strip-notebooks pre-commit-all-files

.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf $(DIST_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.pyo" -exec rm -f {} \;
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .nox
