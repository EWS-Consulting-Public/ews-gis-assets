from __future__ import annotations

import contextlib
from pathlib import Path

from ews_gis_assets.austro_control import get_austro_control_data
from ews_gis_assets.helpers import is_data_updated

OUTPUT_DIR = Path("data")
FILE_NAME = "austro_control_icao"
HASH_FILE = OUTPUT_DIR / f"{FILE_NAME}.hash"


def main():
    """Main method for the script."""
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)

    # Download the GeoJSON file
    gdf, filename = get_austro_control_data(data_path=OUTPUT_DIR)

    if filename and filename.is_file():
        with contextlib.suppress(OSError):
            filename.unlink()

    if gdf is None:
        raise RuntimeError("Failed to download Austro Control data.")

    # Check if data has changed (once for all formats)
    if not is_data_updated(gdf, HASH_FILE):
        print("No changes detected. Exiting without saving files.")
        return

    # Save data to local files in multiple formats
    save_exts = [
        (".geojson", "GeoJSON"),
        (".gpkg", "GPKG"),
    ]
    for suffix, driver in save_exts:
        file_path = OUTPUT_DIR / f"{FILE_NAME}{suffix}"
        gdf.to_file(file_path, driver=driver)
        print(f"Saved {driver} file: {file_path}")

    print("Changes detected. Files updated and can be pushed to the repository.")


if __name__ == "__main__":
    main()
