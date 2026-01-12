from __future__ import annotations

import geopandas as gpd
import pandas as pd
import requests

from ews_gis_assets.constants import NOE_GEOJSON_URL


def download_noe_geojson() -> gpd.GeoDataFrame | None:
    """Download and save NOE GeoJSON data."""

    data = None
    try:
        resp = requests.get(NOE_GEOJSON_URL)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"Error downloading NOE GeoJSON data: {e}")
        return None

    if not isinstance(data, dict) or "features" not in data:
        print("Invalid GeoJSON data received.")
        return None

    gdf = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")
    gdf = gdf.drop(columns=["_fulltext", "_title", "_zoomscale"], errors="ignore")

    # gdf.dtypes.astype("str").to_dict()
    dtypes = {
        "Kennzeichen (UVP)": "category",
        "Kennzeichen (ER)": "category",
        "Rechtsmaterie": "category",
        "Betreiber": "category",
        "Vorhaben": "category",
        "Datum Genehmigungsantrag": "date",
        "Datum Entscheidung 1. Instanz (Bescheid)": "date",
        "Datum Fertigstellungsmeldung": "date",
        "Status": "category",
        "Änderung": "category",
        "Repowering": "category",
        "Name der WKA": "category",
        "Leistung der WKA [MW]": "float",
        "Gesamtleistung [MW]": "float",
        "Gesamthöhe der WKA [m]": "float",
        "Type": "category",
        "Grundstücks-Nummer": "category",
        "Katastralgemeinde": "category",
        "Gemeinde": "category",
        "Bezirk": "category",
        "Hauptregion": "category",
        "KG-Nummer": "int",
        "Koordinaten Länge [WGS 84]": "float",
        "Koordinaten Breite [WGS 84]": "float",
        "Zusatzinformation": "category",
        "Stand": "category",
    }

    # deterministic ordering of columns
    gdf = gdf[[*dtypes.keys(), "geometry"]]

    int_cols = [col for col, dtype in dtypes.items() if dtype == "int"]
    float_cols = [col for col, dtype in dtypes.items() if dtype == "float"]
    date_cols = [col for col, dtype in dtypes.items() if dtype == "date"]
    category_cols = [col for col, dtype in dtypes.items() if dtype == "category"]
    unmapped_cols = [col for col in gdf.columns if col not in dtypes]

    # Remove geometry column from unmapped cols
    if "geometry" in unmapped_cols:
        unmapped_cols.remove("geometry")

    if unmapped_cols:
        raise ValueError(f"Unmapped columns found: {unmapped_cols}")

    # Replace , by dots in float columns abd convert to float
    # We use pd.to_numeric with errors='coerce' to handle non-convertible values
    for col in int_cols:
        s = gdf[col]
        s = s.where(s.notnull(), None)
        gdf[col] = s.astype("int")

    # Replace , by dots in float columns abd convert to float
    # We use pd.to_numeric with errors='coerce' to handle non-convertible values
    for col in float_cols:
        s = gdf[col]
        s = s.where(s.notnull(), None)
        gdf[col] = pd.to_numeric(s.str.replace(",", "."), errors="raise").round(6)

    # Convert date columns to datetime
    for col in date_cols:
        s = gdf[col]
        s = s.where(s.notnull(), None)
        gdf[col] = pd.to_datetime(s, errors="raise", format="%d.%m.%Y")

    # Convert categorical columns to category dtype
    for col in category_cols:
        s = gdf[col]
        s = s.where(s.notnull(), None)
        gdf[col] = s.str.strip().astype("category")

    # Replace Lat / Lon with geometry coordinates
    gdf["Koordinaten Länge [WGS 84]"] = gdf.geometry.x.round(6)
    gdf["Koordinaten Breite [WGS 84]"] = gdf.geometry.y.round(6)

    # Check duplicated values of key tuple formed by ["Vorhaben", "Name der WKA"]
    key_cols = [
        "Vorhaben",
        "Name der WKA",
        "Koordinaten Länge [WGS 84]",
        "Koordinaten Breite [WGS 84]",
    ]
    key = gdf[key_cols].apply(tuple, axis=1)
    duplicates = key[key.duplicated(keep=False)]
    if not duplicates.empty:
        print(f"Size before removing duplicates: {len(gdf)}")
        print("Duplicated key values found:")
        print(duplicates)
        # Only keep the first occurrence of each duplicated key
        key = key.drop_duplicates(keep="first")
        gdf = gdf.loc[key.index]
        print(f"Size after removing duplicates: {len(gdf)}")
        # raise ValueError("Duplicated key values found.")

    # We need to sort in a defined order to have consistent output
    gdf = gdf.sort_values(by=["Vorhaben", "Name der WKA"]).reset_index(drop=True)

    return gdf
