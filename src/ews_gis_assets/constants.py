from __future__ import annotations

NOE_GEOJSON_URL = "https://atlas.noe.gv.at/atlas/api/rest/services/ags_raumordnung__energie@atlas_raumordnung/queries/windkraftanlagen/query?f=json&queryId=windkraftanlagen"

# NÖ GeoServer OGD WFS (EPSG:4326 GeoJSON). Same family as the Atlas WTG layer.
NOE_WFS_GEOJSON = (
    "https://sdi.noe.gv.at/at.gv.noe.geoserver/OGD/wfs"
    "?request=GetFeature&version=1.1.0"
    "&srsName=EPSG:4326"
    "&outputFormat=application/json"
    "&typeName={layer}"
)
NOE_WIND_ZONES_LAYER = "OGD:RRU_WIND_ZONEN_P20_ROG14"
NOE_PV_ZONES_LAYER = "OGD:RRU_PV_ZONEN_P20_ROG14"

# Styria SAPRO Windenergie Zone — INSPIRE WFS (EPSG:4258 GeoJSON).
STYRIA_SAPRO_WIND_WFS = (
    "https://haleconnect.com/ows/services/org.926.334e9873-2470-4934-8a7b-f3c645fb2d6b_wfs"
    "?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature"
    "&TYPENAMES=am:ManagementRestrictionOrRegulationZone"
    "&outputFormat=application/json"
)

# Styria SAPRO Windenergie Bereich — plan extent shapefile (EPSG:4258).
STYRIA_SAPRO_BEREICH_ZIP = (
    "https://service.stmk.gv.at/ogd/OGD_Data_ABT17/geoinformation/SAPRO_Windenergie_bereich.zip"
)

# OÖ Windkraftmasterplan Ausschlusszone — DORIS shapefile zip (EPSG:31255).
OOE_WIND_EXCLUSION_ZIP = (
    "https://e-gov.ooe.gv.at/at.gv.ooe.dorisdaten/DORIS_U/WINDKRAFT_AUSSCHLUSSZONE.zip"
)

# Kärnten RED III Windkraft-Beschleunigungszonen — OGD shapefile zip (EPSG:31258).
KTN_RED_III_WIND_ZIP = (
    "https://gis.ktn.gv.at/OGD/Geographie_Planung/RED_III_Windkraftbeschleunigungszone.zip"
)
