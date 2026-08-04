from __future__ import annotations

from pathlib import Path

from ews_gis_assets.helpers import publish_dataset
from ews_gis_assets.zones import download_noe_wind_zones

OUTPUT_DIR = Path("data")
FILE_NAME = "noe_wind_zones"


def main():
    gdf = download_noe_wind_zones()
    publish_dataset(gdf, OUTPUT_DIR, FILE_NAME)


if __name__ == "__main__":
    main()
