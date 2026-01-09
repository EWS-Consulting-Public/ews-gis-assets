from __future__ import annotations

import hashlib
from pathlib import Path

import geopandas as gpd
import pandas as pd
from folium import Map


def show_folium_safe(m: Map, height=500):
    """
    Displays a Folium map in a safe IFrame using Base64 encoding.
    This avoids "Trusted" errors, file path issues, and CSS leakage.

    See: https://github.com/microsoft/vscode/issues/266193#issuecomment-3571155896
    """

    import base64

    from IPython.display import IFrame, display

    # 1. Get the raw HTML string of the map
    html_content = m.get_root().render()

    # 2. Encode the HTML to base64
    # This allows us to put the entire map "inside" the URL string
    encoded = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")

    # 3. Create a Data URI
    data_uri = f"data:text/html;charset=utf-8;base64,{encoded}"

    # 4. Display the IFrame
    # We use width='100%' to fill the cell width, but the CSS is trapped inside
    display(IFrame(src=data_uri, width="100%", height=height))


def calculate_file_hash(file_path: Path) -> str:
    """Calculate the SHA256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with Path(file_path).open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def calculate_geodata_hash(file_path: Path) -> str:
    """Calculate a content hash for geodata files (GPKG, GeoJSON) ignoring metadata."""
    gdf = gpd.read_file(file_path)
    # Hash the actual data content using pandas hash_pandas_object
    # This ignores file metadata and only hashes the actual data
    content_hash = pd.util.hash_pandas_object(gdf, index=True).sum()
    return str(content_hash)


def calculate_gdf_hash(gdf: gpd.GeoDataFrame) -> str:
    """Calculate a content hash for a GeoDataFrame."""
    content_hash = pd.util.hash_pandas_object(gdf, index=True).sum()
    return str(content_hash)


def is_data_updated(gdf: gpd.GeoDataFrame, hash_file: Path) -> bool:
    """Check if the GeoDataFrame differs from the previous version."""
    new_hash = calculate_gdf_hash(gdf)

    print(f"Using hash file: {hash_file}")

    # Check if the hash file exists
    if hash_file.exists():
        with hash_file.open("r") as f:
            last_hash = f.read().strip()
            if new_hash == last_hash:
                print("Data is identical to the previous version. No update needed.")
                return False

    # Save the new hash for future comparisons
    with hash_file.open("w") as f:
        f.write(new_hash)
    print("New data detected. Updating files...")
    return True


def is_file_updated(new_file: Path) -> bool:
    """Check if the downloaded file differs from the previous version."""
    file_extension = new_file.suffix.lstrip(".").upper()

    # For geodata files (GPKG, GeoJSON), use content hashing instead of file hashing
    if new_file.suffix.lower() in [".gpkg", ".geojson"]:
        new_hash = calculate_geodata_hash(new_file)
    else:
        # For other files, use file hash
        new_hash = calculate_file_hash(new_file)

    hash_file = Path(new_file).with_suffix(new_file.suffix + ".hash")
    print(f"Using hash file: {hash_file}")

    # Check if the hash file exists
    if hash_file.exists():
        with hash_file.open("r") as f:
            last_hash = f.read().strip()
            if new_hash == last_hash:
                # File has not changed
                print(
                    f"{file_extension} file is identical to the previous version. No update needed."
                )
                return False
    # Save the new hash for future comparisons
    with hash_file.open("w") as f:
        f.write(new_hash)
    print(f"New {file_extension} file detected. Updating...")
    return True
