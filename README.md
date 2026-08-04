# ews-gis-assets

GIS assets for EWS-Consulting

This repository automatically downloads and publishes geospatial datasets from various Austrian sources, making them easily accessible in standard GIS formats.

## 🗺️ Available Datasets

### Windkraftanlagen Niederösterreich (Wind Turbines in Lower Austria)

Daily updated dataset of wind turbine locations in Lower Austria from the [NÖ Atlas](https://atlas.noe.gv.at/).

**Download Links** (stable latest release CDN):

- **GeoJSON**: [`…/releases/latest/download/windkraftanlagen.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.geojson)
- **GeoPackage (GPKG)**: [`…/releases/latest/download/windkraftanlagen.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg)

Also on `main`: [`data/windkraftanlagen.geojson`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.geojson)

**Update Frequency**: Checked daily at midnight UTC; released when content hashes change

### Austro Control ICAO Obstacle Dataset (Wind Turbines - Austria)

Aviation obstacle data for wind turbines across Austria from [Austro Control](https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao). Includes operational, under construction, and planned wind turbines.

**Download Links** (stable latest release CDN):

- **GeoJSON**: [`…/releases/latest/download/austro_control_icao.geojson`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.geojson)
- **GeoPackage (GPKG)**: [`…/releases/latest/download/austro_control_icao.gpkg`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/austro_control_icao.gpkg)

Also on `main`: [`data/austro_control_icao.geojson`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/austro_control_icao.geojson)

**Update Frequency**: Checked daily; typically ~monthly when Austro Control publishes a new package

**Attributes**: Name, Wind Farm, Status (Operating/UnderConstruction/Plan/Approved), Elevation, Height, Geographic coordinates, Accuracy metrics

## 📋 Available Formats

Data is provided in **GeoJSON** and **GeoPackage (GPKG)** formats.

> **Note:** KMZ/KML formats are not exported due to large file sizes and limited attribute support. For Google Earth visualization, we recommend using **QGIS** to load the GPKG files and export to KMZ with custom styling and filtered attributes as needed.

## 🔄 How It Works

1. **Automated Downloads**: A [scheduled GitHub Action](https://github.com/EWS-Consulting-Public/ews-gis-assets/actions/workflows/update.yaml) runs daily to fetch the latest data from source APIs
2. **Smart Updates**: Uses content hashing (via pandas) to detect data changes
3. **Multi-Format Export**: Automatically converts and saves data in multiple GIS formats (GeoJSON, GPKG)
4. **Commit + Release**: When hashes/files change, commits to `main` and publishes a GitHub Release (all GeoJSON/GPKG assets) so [`/releases/latest/download/…`](https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest) stays current

## 🛠️ Technical Details

- **Language**: Python 3.12+
- **Key Libraries**: GeoPandas, Pandas, Pyogrio
- **Package Manager**: uv
- **CI/CD**: GitHub Actions

## 📦 Usage

Prefer the **latest release** URLs (stable CDN). `raw.githubusercontent.com/.../main/data/...` also works after each commit.

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
curl -LO https://github.com/EWS-Consulting-Public/ews-gis-assets/releases/latest/download/windkraftanlagen.gpkg
```

## 🚀 Development

### Setup

```bash
# Clone the repository
git clone https://github.com/EWS-Consulting-Public/ews-gis-assets.git
cd ews-gis-assets

# Install dependencies with uv
uv sync --locked --all-extras --dev

# Run the update script
uv run main.py
```
