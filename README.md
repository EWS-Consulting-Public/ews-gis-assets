# ews-gis-assets

GIS assets for EWS-Consulting

This repository automatically downloads and publishes geospatial datasets from various Austrian sources, making them easily accessible in standard GIS formats.

## Available Datasets

Prefer the **latest release** URLs (stable CDN) for downloads. GeoJSON also has a
**map preview** on GitHub (`blob/main/data/…`) — that opens the rendered map in
the browser instead of downloading the file.

Release base: `https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/`

| Dataset | GeoJSON (download · map) | GPKG |
| --- | --- | --- |
| NÖ wind turbines | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/windkraftanlagen.geojson) | [`windkraftanlagen.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg) |
| Austro Control ICAO (WTG, Austria) | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/austro_control_icao.geojson) | [`austro_control_icao.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.gpkg) |
| NÖ Windkraftzonen §20 ROG | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/noe_wind_zones.geojson) | [`noe_wind_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.gpkg) |
| NÖ PV-Zonen §20 ROG | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/noe_pv_zones.geojson) | [`noe_pv_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.gpkg) |
| Steiermark SAPRO Windenergie Zone | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/styria_sapro_wind.geojson) | [`styria_sapro_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.gpkg) |
| Steiermark SAPRO Windenergie Bereich | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_bereich.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/styria_sapro_bereich.geojson) | [`styria_sapro_bereich.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_bereich.gpkg) |
| OÖ Windkraftmasterplan Ausschlusszone | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/ooe_wind_exclusion.geojson) | [`ooe_wind_exclusion.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.gpkg) |
| Kärnten RED III Windkraft-Beschleunigungszonen | [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ktn_red_iii_wind.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/ktn_red_iii_wind.geojson) | [`ktn_red_iii_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ktn_red_iii_wind.gpkg) |

> The GitHub map preview may skip very large GeoJSON files (OÖ exclusion is ~23 MB). Use the GPKG / QGIS path in that case.

### Windkraftanlagen Niederösterreich (Wind Turbines in Lower Austria)

Daily updated point dataset from the [NÖ Atlas](https://atlas.noe.gv.at/).

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/windkraftanlagen.geojson)
- **GeoPackage**: [`windkraftanlagen.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg)

### Austro Control ICAO Obstacle Dataset (Wind Turbines - Austria)

Aviation obstacle data for wind turbines across Austria from [Austro Control](https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao). Includes operational, under construction, and planned wind turbines.

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/austro_control_icao.geojson)
- **GeoPackage**: [`austro_control_icao.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.gpkg)

Typically updates ~monthly when Austro Control publishes a new package.

**Attributes**: Name, Wind Farm, Status (Operating/UnderConstruction/Plan/Approved), Elevation, Height, Geographic coordinates, Accuracy metrics

### NÖ Windkraftzonen (§20 ROG)

Planning zones where municipalities may designate Grünland–Windkraftanlage (Gwka). Source: [NÖ OGD](https://www.noe.gv.at/noe/OGD_Detailseite.html?id=2df95d9f-5914-4ec5-a21c-c0f06c9a151e) / GeoServer WFS.

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/noe_wind_zones.geojson)
- **GeoPackage**: [`noe_wind_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.gpkg)

### NÖ PV-Zonen im Grünland (§20 ROG)

Freiflächen-PV planning zones. Same NÖ GeoServer OGD family.

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/noe_pv_zones.geojson)
- **GeoPackage**: [`noe_pv_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.gpkg)

### Steiermark SAPRO Windenergie Zone

Vorrangzonen from the Styrian Sachprogramm Windenergie (INSPIRE WFS).

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/styria_sapro_wind.geojson)
- **GeoPackage**: [`styria_sapro_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.gpkg)

### Steiermark SAPRO Windenergie Bereich

Plan Geltungsbereich (extent) for the same Styrian SAPRO Windenergie programme.

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_bereich.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/styria_sapro_bereich.geojson)
- **GeoPackage**: [`styria_sapro_bereich.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_bereich.gpkg)

### OÖ Windkraftmasterplan Ausschlusszone

Upper Austria exclusion zone from DORIS (shapefile zip).

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/ooe_wind_exclusion.geojson)
- **GeoPackage**: [`ooe_wind_exclusion.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.gpkg)

### Kärnten RED III Windkraft-Beschleunigungszonen

Acceleration zones under K-ROG / RED III (OGD shapefile).

- **GeoJSON**: [`download`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ktn_red_iii_wind.geojson) · [![map](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/EWS-Consulting-Public/ews-gis-assets/blob/main/data/ktn_red_iii_wind.geojson)
- **GeoPackage**: [`ktn_red_iii_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ktn_red_iii_wind.gpkg)


## Available Formats

Data is provided in **GeoJSON** and **GeoPackage (GPKG)** formats.

> **Note:** KMZ/KML formats are not exported due to large file sizes and limited attribute support. For Google Earth visualization, we recommend using **QGIS** to load the GPKG files and export to KMZ with custom styling and filtered attributes as needed.

## How It Works

1. **Automated Downloads**: A [scheduled GitHub Action](https://github.com/EWS-Consulting-Public/ews-gis-assets/actions/workflows/update.yaml) runs daily to fetch the latest data from source APIs. Each downloader runs independently — one upstream outage does not block the others; successful updates still commit/release, and the job fails at the end if any script failed.
2. **Smart Updates**: Uses content hashing (via pandas) to detect data changes
3. **Multi-Format Export**: Automatically converts and saves data in multiple GIS formats (GeoJSON, GPKG)
4. **Commit + Release**: When hashes/files change, commits to `main` and publishes a GitHub Release (all present GeoJSON/GPKG assets) so [`/releases/latest/download/…`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest) stays current

## Technical Details

- **Language**: Python 3.12+
- **Key Libraries**: GeoPandas, Pandas, Pyogrio
- **Package Manager**: uv
- **CI/CD**: GitHub Actions

## Usage

### Example with GeoPandas

```python
import geopandas as gpd

url = "https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson"
gdf = gpd.read_file(url)
print(gdf.head())
```

### Example with QGIS

Add as a vector layer using the GeoJSON or GPKG **latest release** URL in the "Add Vector Layer" dialog.

### Example with curl

```bash
# Follow redirects from the stable latest URL
curl -LO https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson
curl -LO https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.geojson
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/EWS-Consulting-Public/ews-gis-assets.git
cd ews-gis-assets

# Install dependencies with uv
uv sync --locked --all-extras --dev

# Run downloaders (each writes under data/ when content hashes change)
uv run download_noe_wind_turbines.py
uv run download_austro_control.py
uv run download_noe_wind_zones.py
uv run download_noe_pv_zones.py
uv run download_styria_sapro_wind.py
uv run download_styria_sapro_bereich.py
uv run download_ooe_wind_exclusion.py
uv run download_ktn_red_iii_wind.py
```
