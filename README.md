# ews-gis-assets

GIS assets for EWS-Consulting

This repository automatically downloads and publishes geospatial datasets from various Austrian sources, making them easily accessible in standard GIS formats.

## Available Datasets

Prefer the **latest release** URLs (stable CDN). `raw.githubusercontent.com/.../main/data/...` also works after each commit.

Base: `https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/`

| Dataset | Latest GeoJSON | Latest GPKG |
| --- | --- | --- |
| NÖ wind turbines | [`windkraftanlagen.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson) | [`windkraftanlagen.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg) |
| Austro Control ICAO (WTG, Austria) | [`austro_control_icao.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.geojson) | [`austro_control_icao.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.gpkg) |
| NÖ Windkraftzonen §20 ROG | [`noe_wind_zones.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.geojson) | [`noe_wind_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.gpkg) |
| NÖ PV-Zonen §20 ROG | [`noe_pv_zones.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.geojson) | [`noe_pv_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.gpkg) |
| Steiermark SAPRO Windenergie Zone | [`styria_sapro_wind.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.geojson) | [`styria_sapro_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.gpkg) |
| OÖ Windkraftmasterplan Ausschlusszone | [`ooe_wind_exclusion.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.geojson) | [`ooe_wind_exclusion.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.gpkg) |

### Windkraftanlagen Niederösterreich (Wind Turbines in Lower Austria)

Daily updated point dataset from the [NÖ Atlas](https://atlas.noe.gv.at/).

- **GeoJSON**: [`windkraftanlagen.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson)
- **GeoPackage**: [`windkraftanlagen.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg)

### Austro Control ICAO Obstacle Dataset (Wind Turbines - Austria)

Aviation obstacle data for wind turbines across Austria from [Austro Control](https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao). Includes operational, under construction, and planned wind turbines.

- **GeoJSON**: [`austro_control_icao.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.geojson)
- **GeoPackage**: [`austro_control_icao.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.gpkg)

Typically updates ~monthly when Austro Control publishes a new package.

**Attributes**: Name, Wind Farm, Status (Operating/UnderConstruction/Plan/Approved), Elevation, Height, Geographic coordinates, Accuracy metrics

### NÖ Windkraftzonen (§20 ROG)

Planning zones where municipalities may designate Grünland–Windkraftanlage (Gwka). Source: [NÖ OGD](https://www.noe.gv.at/noe/OGD_Detailseite.html?id=2df95d9f-5914-4ec5-a21c-c0f06c9a151e) / GeoServer WFS.

- **GeoJSON**: [`noe_wind_zones.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.geojson)
- **GeoPackage**: [`noe_wind_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_wind_zones.gpkg)

### NÖ PV-Zonen im Grünland (§20 ROG)

Freiflächen-PV planning zones. Same NÖ GeoServer OGD family.

- **GeoJSON**: [`noe_pv_zones.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.geojson)
- **GeoPackage**: [`noe_pv_zones.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/noe_pv_zones.gpkg)

### Steiermark SAPRO Windenergie Zone

Vorrangzonen from the Styrian Sachprogramm Windenergie (INSPIRE WFS).

- **GeoJSON**: [`styria_sapro_wind.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.geojson)
- **GeoPackage**: [`styria_sapro_wind.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/styria_sapro_wind.gpkg)

### OÖ Windkraftmasterplan Ausschlusszone

Upper Austria exclusion zone from DORIS (shapefile zip).

- **GeoJSON**: [`ooe_wind_exclusion.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.geojson)
- **GeoPackage**: [`ooe_wind_exclusion.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/ooe_wind_exclusion.gpkg)

## Available Formats

Data is provided in **GeoJSON** and **GeoPackage (GPKG)** formats.

> **Note:** KMZ/KML formats are not exported due to large file sizes and limited attribute support. For Google Earth visualization, we recommend using **QGIS** to load the GPKG files and export to KMZ with custom styling and filtered attributes as needed.

## How It Works

1. **Automated Downloads**: A [scheduled GitHub Action](https://github.com/EWS-Consulting-Public/ews-gis-assets/actions/workflows/update.yaml) runs daily to fetch the latest data from source APIs
2. **Smart Updates**: Uses content hashing (via pandas) to detect data changes
3. **Multi-Format Export**: Automatically converts and saves data in multiple GIS formats (GeoJSON, GPKG)
4. **Commit + Release**: When hashes/files change, commits to `main` and publishes a GitHub Release (all GeoJSON/GPKG assets) so [`/releases/latest/download/…`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest) stays current

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
uv run download_ooe_wind_exclusion.py
```
