# ews-gis-assets

GIS assets for EWS-Consulting

This repository automatically downloads and publishes geospatial datasets from various Austrian sources, making them easily accessible in standard GIS formats.

## 🗺️ Available Datasets

### Windkraftanlagen Niederösterreich (Wind Turbines in Lower Austria)

Daily updated dataset of wind turbine locations in Lower Austria from the [NÖ Atlas](https://atlas.noe.gv.at/).

**Download Links:**

- **GeoJSON**: [`https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.geojson`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.geojson)
- **GeoPackage (GPKG)**: [`https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.gpkg`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.gpkg)

**Update Frequency**: Daily at midnight UTC (via GitHub Actions)

### Austro Control ICAO Obstacle Dataset (Wind Turbines - Austria)

Aviation obstacle data for wind turbines across Austria from [Austro Control](https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao). Includes operational, under construction, and planned wind turbines.

**Download Links:**

- **GeoJSON**: [`https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/austro_control_icao.geojson`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/austro_control_icao.geojson)
- **GeoPackage (GPKG)**: [`https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/austro_control_icao.gpkg`](https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/austro_control_icao.gpkg)

**Update Frequency**: Daily at midnight UTC (via GitHub Actions)

**Attributes**: Name, Wind Farm, Status (Operating/UnderConstruction/Plan/Approved), Elevation, Height, Geographic coordinates, Accuracy metrics

## 🔄 How It Works

1. **Automated Downloads**: A scheduled GitHub Action runs daily to fetch the latest data from source APIs
2. **Smart Updates**: Uses content hashing (via pandas) to detect actual data changes, ignoring metadata
3. **Multi-Format Export**: Automatically converts and saves data in multiple GIS formats (GeoJSON, GPKG)
4. **Version Control**: Only commits when actual data changes are detected, keeping the repository clean

## 🛠️ Technical Details

- **Language**: Python 3.12+
- **Key Libraries**: GeoPandas, Pandas, Pyogrio
- **Package Manager**: uv
- **CI/CD**: GitHub Actions

## 📦 Usage

You can directly reference these files in your GIS applications, scripts, or workflows using the raw GitHub URLs above.

### Example with GeoPandas

```python
import geopandas as gpd

# Load data directly from GitHub
url = "https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.geojson"
gdf = gpd.read_file(url)
print(gdf.head())
```

### Example with QGIS

Add as a vector layer using the GeoJSON or GPKG URL directly in the "Add Vector Layer" dialog.

### Example with curl

```bash
# Download GeoJSON
curl -O https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.geojson

# Download GPKG
curl -O https://raw.githubusercontent.com/EWS-Consulting-Public/ews-gis-assets/main/data/windkraftanlagen.gpkg
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
