from __future__ import annotations

from pathlib import Path

from ews_gis_assets.helpers import publish_dataset
from ews_gis_assets.noe import download_noe_geojson

OUTPUT_DIR = Path("data")
FILE_NAME = "windkraftanlagen"


def main():
    """Download NÖ wind turbines and publish when content (ex-Stand) changes."""
    gdf = download_noe_geojson()
    if gdf is None:
        raise RuntimeError("Failed to download NOE GeoJSON data.")
    publish_dataset(gdf, OUTPUT_DIR, FILE_NAME)


if __name__ == "__main__":
    main()
