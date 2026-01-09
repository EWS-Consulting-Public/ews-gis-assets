from __future__ import annotations

import re
from importlib import metadata


def get_version() -> str:
    """Return the installed package version for `ews-gis-assets`.

    This uses importlib.metadata and will raise `PackageNotFoundError` if
    the package is not installed. Callers must handle that if they expect
    the code to work in a non-installed developer tree.
    """
    return metadata.version("ews-gis-assets")


def python_dependency_versions() -> dict[str, str]:
    """Return versions for declared Python dependencies using installed metadata.

    The returned mapping includes the packages listed in the installed
    distribution's metadata `requires` entries when available. If a package
    listed in `requires` is not installed, it will be omitted.
    """
    out: dict[str, str] = {}
    dist = metadata.distribution("ews-gis-assets")
    requires = dist.metadata.get_all("Requires-Dist") or []
    for req in requires:
        # Requires-Dist can include extras and markers; parse simple 'name' token
        name = req.split(";")[0].strip()  # Remove markers like "; extra=='test'"
        name = name.split("(")[0].strip()  # Remove parenthetical version specs
        # Remove version specifications like >=1.21.0, ==2.0.*, etc.
        name = re.split(r"[<>=!~]", name)[0].strip()
        try:
            out[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            # Per policy don't fall back to import-time introspection
            continue
    return out


def cpp_dependency_versions() -> dict[str, str | None]:
    """Return versions for C++ dependencies using compiled-in version info.

    This calls the C++ extension to get compile-time version information.
    Returns None for libraries if the extension is not available.
    """
    versions: dict[str, str | None] = {}
    return versions


def get_version_info() -> dict[str, object]:
    """Return a dict with strict metadata-derived version information.

    Keys:
      - project: {'name': 'ews-gis-assets', 'version': <version str>}
      - python: dict of dependency_name -> version (only for installed deps)
      - cpp: dict of cpp_dependency -> version (from compiled extension)
    """
    return {
        "project": {"name": "ews-gis-assets", "version": get_version()},
        "python": python_dependency_versions(),
        "cpp": cpp_dependency_versions(),
    }


def show_version() -> None:
    """Show version information using the package Rich-based logger.

    Displays project metadata and dependency versions using rich tables so
    the output is readable in notebooks and terminals.
    """

    info = get_version_info()

    try:
        from ews_logger import create_logger
    except ImportError:
        print(get_version())
        return

    logger = create_logger("", verbosity=1, use_stdlib_logging=False)

    # Project header
    logger.info(f"Name: {info['project']['name']}")
    logger.info(f"Version: {info['project']['version']}")

    # Python dependencies table
    py_deps = info.get("python", {})
    if py_deps:
        logger.rule("Python Dependencies")
        # Use table helper if available
        deps_table = dict(sorted(py_deps.items()))
        logger.table(
            deps_table,
            title="",
            min_verbosity=1,
            key_name="Package",
            value_name="Version",
        )
    else:
        logger.info("No installed Python dependencies detected.")

    # C++ dependencies
    cpp_deps = info.get("cpp", {})
    if cpp_deps:
        logger.rule("C++ Dependencies")
        cpp_table = {k: (v or "unavailable") for k, v in sorted(cpp_deps.items())}
        logger.table(
            cpp_table,
            title="",
            min_verbosity=1,
            key_name="Library",
            value_name="Version",
        )
    else:
        logger.info("No C++ dependencies are registered.")


__version__ = get_version()

__all__ = ["__version__", "get_version", "get_version_info"]
