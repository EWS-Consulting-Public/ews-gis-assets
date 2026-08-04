from __future__ import annotations

from pathlib import Path

from ews_gis_assets.helpers import publish_dataset
from ews_gis_assets.zones import download_ooe_wind_exclusion

OUTPUT_DIR = Path("data")
FILE_NAME = "ooe_wind_exclusion"


def main():
    gdf = download_ooe_wind_exclusion()
    publish_dataset(gdf, OUTPUT_DIR, FILE_NAME)


if __name__ == "__main__":
    main()
