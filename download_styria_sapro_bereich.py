from __future__ import annotations

from pathlib import Path

from ews_gis_assets.helpers import publish_dataset
from ews_gis_assets.zones import download_styria_sapro_bereich

OUTPUT_DIR = Path("data")
FILE_NAME = "styria_sapro_bereich"


def main():
    gdf = download_styria_sapro_bereich()
    publish_dataset(gdf, OUTPUT_DIR, FILE_NAME)


if __name__ == "__main__":
    main()
