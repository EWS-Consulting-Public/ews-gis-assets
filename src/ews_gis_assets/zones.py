from __future__ import annotations

import io
import tempfile
import zipfile
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests

from ews_gis_assets.constants import (
    KTN_RED_III_WIND_ZIP,
    NOE_PV_ZONES_LAYER,
    NOE_WFS_GEOJSON,
    NOE_WIND_ZONES_LAYER,
    OOE_WIND_EXCLUSION_ZIP,
    STYRIA_SAPRO_BEREICH_ZIP,
    STYRIA_SAPRO_WIND_WFS,
)
from ews_gis_assets.helpers import to_wgs84


def _fetch_geojson(url: str) -> gpd.GeoDataFrame:
    resp = requests.get(url, timeout=180)
    resp.raise_for_status()
    gdf = gpd.read_file(io.BytesIO(resp.content))
    if gdf.empty:
        raise RuntimeError(f"Empty GeoJSON from {url}")
    return gdf


def _read_shapefile_zip(url: str) -> gpd.GeoDataFrame:
    """Download a zip that contains exactly one .shp (+ siblings) and read it."""
    resp = requests.get(url, timeout=180)
    resp.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        names = [n for n in zf.namelist() if n.lower().endswith(".shp")]
        if len(names) != 1:
            raise RuntimeError(f"Expected one .shp in {url}, found: {names}")
        with tempfile.TemporaryDirectory() as tmp:
            zf.extractall(tmp)
            gdf = gpd.read_file(Path(tmp) / names[0])
    if gdf.empty:
        raise RuntimeError(f"Empty shapefile from {url}")
    return gdf


def _as_date(series: pd.Series) -> pd.Series:
    """Date-only values — drop timezone noise that would churn content hashes."""
    s = pd.to_datetime(series, errors="raise", utc=True)
    return s.dt.tz_convert(None).dt.normalize()


def download_noe_wind_zones() -> gpd.GeoDataFrame:
    """NÖ Windkraftzonen §20 ROG — polygons where Gwka widmung may still be set."""
    url = NOE_WFS_GEOJSON.format(layer=NOE_WIND_ZONES_LAYER)
    gdf = _fetch_geojson(url)
    gdf = to_wgs84(gdf)

    keep = [
        "ID",
        "ZONE",
        "AREA_HA",
        "COMMUNITIES",
        "LEGALFOUNDATIONDATE",
        "LEGISLATIONCODE",
        "LEGISLATIONTITLE",
        "LASTUPDATE",
        "geometry",
    ]
    missing = [c for c in keep if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected NÖ wind-zone schema, missing: {missing}")

    gdf = gdf[keep].copy()
    gdf["ID"] = gdf["ID"].astype("int64")
    gdf["AREA_HA"] = pd.to_numeric(gdf["AREA_HA"], errors="raise").round(6)
    for col in ("ZONE", "COMMUNITIES", "LEGISLATIONCODE", "LEGISLATIONTITLE"):
        gdf[col] = gdf[col].astype("string").str.replace(r"\s+", " ", regex=True).str.strip()
    gdf["LEGALFOUNDATIONDATE"] = _as_date(gdf["LEGALFOUNDATIONDATE"])
    gdf["LASTUPDATE"] = _as_date(gdf["LASTUPDATE"])
    return gdf.sort_values("ZONE").reset_index(drop=True)


def download_noe_pv_zones() -> gpd.GeoDataFrame:
    """NÖ PV-Zonen im Grünland §20 ROG — Freiflächen-PV planning zones."""
    url = NOE_WFS_GEOJSON.format(layer=NOE_PV_ZONES_LAYER)
    gdf = _fetch_geojson(url)
    gdf = to_wgs84(gdf)

    keep = [
        "GID",
        "ZONENAME",
        "COMMUNITY",
        "DISTRICT",
        "LEGALFOUNDATIONDATE",
        "LEGISLATIONCODE",
        "LEGISLATIONTITLE",
        "LASTUPDATE",
        "geometry",
    ]
    missing = [c for c in keep if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected NÖ PV-zone schema, missing: {missing}")

    gdf = gdf[keep].copy()
    for col in ("GID", "ZONENAME", "COMMUNITY", "DISTRICT", "LEGISLATIONCODE", "LEGISLATIONTITLE"):
        gdf[col] = gdf[col].astype("string").str.replace(r"\s+", " ", regex=True).str.strip()
    gdf["LEGALFOUNDATIONDATE"] = _as_date(gdf["LEGALFOUNDATIONDATE"])
    gdf["LASTUPDATE"] = _as_date(gdf["LASTUPDATE"])
    return gdf.sort_values("ZONENAME").reset_index(drop=True)


def download_styria_sapro_wind() -> gpd.GeoDataFrame:
    """Steiermark SAPRO Windenergie Zone — Vorrangzonen from INSPIRE WFS."""
    gdf = _fetch_geojson(STYRIA_SAPRO_WIND_WFS)
    gdf = to_wgs84(gdf)

    # INSPIRE nests contact fields into pipe-separated GeoJSON property names;
    # keep only zone identity + legal reference.
    rename = {
        "localId": "local_id",
        "text": "zone_name",
        "name": "plan_name",
        "Date": "publication_date",
        "link": "ris_link",
    }
    missing = [c for c in rename if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected Styria SAPRO schema, missing: {missing}")

    gdf = gdf[[*rename.keys(), "geometry"]].rename(columns=rename)
    gdf["local_id"] = gdf["local_id"].astype("int64")
    for col in ("zone_name", "plan_name", "ris_link"):
        gdf[col] = gdf[col].astype("string").str.replace(r"\s+", " ", regex=True).str.strip()
    gdf["publication_date"] = _as_date(gdf["publication_date"])
    return gdf.sort_values("local_id").reset_index(drop=True)


def download_styria_sapro_bereich() -> gpd.GeoDataFrame:
    """Steiermark SAPRO Windenergie Bereich — plan Geltungsbereich extent."""
    gdf = _read_shapefile_zip(STYRIA_SAPRO_BEREICH_ZIP)
    gdf = to_wgs84(gdf)

    rename = {
        "OBJECTID": "object_id",
        "Name": "name",
        "Shape_Leng": "shape_length",
        "Shape_Area": "shape_area",
    }
    missing = [c for c in rename if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected Styria SAPRO Bereich schema, missing: {missing}")

    gdf = gdf[[*rename.keys(), "geometry"]].rename(columns=rename)
    gdf["object_id"] = gdf["object_id"].astype("int64")
    gdf["name"] = gdf["name"].astype("string").str.strip()
    gdf["shape_length"] = pd.to_numeric(gdf["shape_length"], errors="raise")
    gdf["shape_area"] = pd.to_numeric(gdf["shape_area"], errors="raise")
    return gdf.sort_values("object_id").reset_index(drop=True)


def download_ooe_wind_exclusion() -> gpd.GeoDataFrame:
    """OÖ Windkraftmasterplan Ausschlusszone — DORIS shapefile (one multipolygon)."""
    gdf = _read_shapefile_zip(OOE_WIND_EXCLUSION_ZIP)
    gdf = to_wgs84(gdf)

    # DBF truncates names; rename to the INSPIRE meanings from the companion GML.
    rename = {
        "ANMERKUNG": "name",
        "SpecificRe": "specific_regulation",
        "Supplement": "supplementary_regulation",
        "Regulation": "regulation_nature",
        "GlobalID": "global_id",
        "InspireID": "inspire_id",
        "ID": "id",
    }
    missing = [c for c in rename if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected OÖ exclusion schema, missing: {missing}")

    gdf = gdf[[*rename.keys(), "geometry"]].rename(columns=rename)
    for col in (
        "name",
        "specific_regulation",
        "supplementary_regulation",
        "regulation_nature",
        "global_id",
        "inspire_id",
    ):
        gdf[col] = gdf[col].astype("string").str.replace(r"\s+", " ", regex=True).str.strip()
    gdf["id"] = gdf["id"].astype("int64")
    return gdf.sort_values("inspire_id").reset_index(drop=True)


def download_ktn_red_iii_wind() -> gpd.GeoDataFrame:
    """Kärnten RED III Windkraft-Beschleunigungszonen — K-ROG / RED III polygons."""
    gdf = _read_shapefile_zip(KTN_RED_III_WIND_ZIP)
    gdf = to_wgs84(gdf)

    rename = {
        "ZONENBEZ": "zone_name",
        "SHAPE_AREA": "shape_area",
        "SHAPE_LEN": "shape_length",
    }
    missing = [c for c in rename if c not in gdf.columns]
    if missing:
        raise ValueError(f"Unexpected Kärnten RED III schema, missing: {missing}")

    gdf = gdf[[*rename.keys(), "geometry"]].rename(columns=rename)
    gdf["zone_name"] = gdf["zone_name"].astype("string").str.strip()
    gdf["shape_area"] = pd.to_numeric(gdf["shape_area"], errors="raise").round(6)
    gdf["shape_length"] = pd.to_numeric(gdf["shape_length"], errors="raise").round(6)
    return gdf.sort_values("zone_name").reset_index(drop=True)
