from __future__ import annotations

import io
import operator
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pyproj
import requests
from bs4 import BeautifulSoup


def get_austro_control_links() -> list[str, str]:
    """
    Get a list (publication_date, url) of available Hindernisdatensatz (ICAO) - Österreich.
    The list sorted in descending order of publication date.
    Source: https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao
    """

    resp = requests.get(
        "https://www.austrocontrol.at/piloten/vor_dem_flug/aim_produkte/hindernisdatensaetze_icao"
    )
    assert resp.status_code == 200
    table = BeautifulSoup(resp.content, "lxml").find("table", attrs={"class": "download_liste"})
    links = table.find_all("a")
    base_url = "https://www.austrocontrol.at/jart/prj3/ac/"
    links = [base_url + _.attrs["href"] for _ in links]
    links = [(k.split("LO_OBS_DS_AREA1_", 1)[1].split("_")[0], k) for k in links]
    links = sorted(links, key=lambda x: x[0])[::-1]
    return links


def clean_name(s):
    if s.startswith("Windpark "):
        return s.replace("Windpark ", "").strip()
    if s.startswith("WP "):
        return s.replace("WP ", "").strip()
    if s.startswith("WKA "):
        return s.replace("WKA ", "").strip()
    if s.startswith("Windturbine "):
        return s.replace("Windturbine ", "").strip()
    if s.startswith("Windkraftanlage"):
        return s.replace("Windkraftanlage ", "").strip()
    return s.strip()


def parse_icao(data: str | bytes) -> gpd.GeoDataFrame:
    root = ET.fromstring(data)

    structs = list(root.iter(tag="{http://www.aixm.aero/schema/5.1.1}VerticalStructure"))
    wtgs = []
    valid_types = {"WINDMILL_FARMS", "WINDMILL"}
    for part in structs:
        p_type = part.find(".//{http://www.aixm.aero/schema/5.1.1}type").text
        if p_type not in valid_types:
            continue
        status = part.find(".//{http://www.aixm.aero/schema/5.1.1}constructionStatus").text.strip()
        wp_name = part.find(".//{http://www.aixm.aero/schema/5.1.1}name").text
        wp_name2 = clean_name(
            part.find(".//{http://www.aixm.aero/schema/5.1.1}Note")
            .find(".//{http://www.aixm.aero/schema/5.1.1}note")
            .text
        )

        for wtg in part.findall(".//{http://www.aixm.aero/schema/5.1.1}VerticalStructurePart"):
            wtgs.append(
                {
                    "WindFarm": wp_name2,
                    "WPID": wp_name,
                    "Name": dict(wtg.items())["{http://www.opengis.net/gml/3.2}id"],
                    "VerticalExtent": wtg.find(
                        ".//{http://www.aixm.aero/schema/5.1.1}verticalExtent"
                    ).text,
                    "VerticalAccuracy": wtg.find(
                        ".//{http://www.aixm.aero/schema/5.1.1}verticalExtentAccuracy"
                    ).text,
                    "HorizontalAccuracy": wtg.find(
                        ".//{http://www.aixm.aero/schema/5.1.1}horizontalAccuracy"
                    ).text,
                    "geometry": wtg.find(".//{http://www.opengis.net/gml/3.2}pos").text.split(" "),
                    "Status": status,
                    "Elevation": wtg.find(".//{http://www.aixm.aero/schema/5.1.1}elevation").text,
                    "Type": wtg.find(".//{http://www.aixm.aero/schema/5.1.1}type").text,
                }
            )

    df = pd.DataFrame.from_records(wtgs)
    df["UID"] = df["Name"].str.split("_", expand=True).iloc[:, 1].astype("int")
    for col in [
        "HorizontalAccuracy",
        "Elevation",
        "VerticalExtent",
        "VerticalAccuracy",
    ]:
        df[col] = df[col].apply(pd.to_numeric, errors="coerce")

    df["TerrainElevation"] = (df["Elevation"] - df["VerticalExtent"]).round(1)
    df["geometry"] = gpd.points_from_xy(
        df["geometry"].apply(operator.itemgetter(1)),
        df["geometry"].apply(operator.itemgetter(0)),
    )
    df["Longitude"] = [_.x for _ in df.geometry]
    df["Latitude"] = [_.y for _ in df.geometry]
    rd = {
        "COMPLETED": "Operating",
        "IN_CONSTRUCTION": "UnderConstruction",
        "MODIFICATION_APPRVD": "ModificationApproved",
        "DEMOLITION_PLANNED": "DemolitionPlanned",
        "CONSTRUCTION_PLANNED": "Plan",
        "CONSTRUCTION_APPRVD": "Approved",
        "OTHER:IN_CONSTRUCTION": "UnderConstruction",
        "OTHER:MODIFICATION_APPRVD": "ModificationApproved",
        "OTHER:DEMOLITION_PLANNED": "DemolitionPlanned",
        "OTHER:CONSTRUCTION_PLANNED": "Plan",
        "OTHER:MODIFICATION_PLANNED": "ModificationPlanned",
        "OTHER:CONSTRUCTION_APPRVD": "Approved",
    }
    df["Status"] = df["Status"].fillna("").apply(lambda _: rd.get(_, _))

    df = gpd.GeoDataFrame(df)
    df.crs = pyproj.crs.crs.CRS.from_epsg(4326)
    assert df.UID.duplicated().sum() == 0
    return df[
        [
            "Name",
            "WPID",
            # "Begin",
            "WindFarm",
            "HorizontalAccuracy",
            "TerrainElevation",
            "Elevation",
            "VerticalExtent",
            "VerticalAccuracy",
            "Type",
            "Status",
            "geometry",
            "Longitude",
            "Latitude",
            "UID",
        ]
    ]


def get_austro_control_data(
    data_path: Path | None = None, list_index: int = 0, overwrite: bool = False
) -> tuple[gpd.GeoDataFrame, Path | None]:
    """
    Retrieve the Hindernisdatensatz dataframe.
    list_index specifies with index to use in the list retrieved from get_bev_links_for_scale
    """
    urls = get_austro_control_links()
    assert list_index < len(urls)
    publication_date, url = urls[list_index]

    print(f"Requesting {str(Path(url).name)!r} ({publication_date})")

    expected_name = (
        "LO_OBS_DS_AREA1_" + url.split("/")[-1].split("LO_OBS_DS_AREA1_")[1].split("_")[0] + ".xml"
    )

    filename = None
    if data_path is not None:
        data_path = data_path.resolve()
        assert data_path.is_dir()
        filename = data_path / expected_name

    ac_source = None
    if ((filename is None) or (not filename.is_file())) or overwrite:
        print(f"Getting Obstacle dataset (ICAO) from {url!s}")
        try:
            resp = requests.get(url)
            with zipfile.ZipFile(io.BytesIO(resp.content)) as zin:
                files = [_ for _ in zin.namelist() if _.endswith(".xml")]
                if len(files) == 1:
                    ac_source = zin.read(files[0])
            if ac_source is None:
                raise RuntimeError("Could not fetch Obstacle dataset (ICAO)")
            if isinstance(filename, Path):
                filename.write_bytes(ac_source)
        except Exception as e:
            ac_source = None
            print(str(e))
    else:
        print(f"Using existing file {str(filename.name)!r}")
        ac_source = filename.read_bytes()

    df_austro = parse_icao(ac_source)
    df_austro["PublicationDate"] = publication_date
    return df_austro, filename
