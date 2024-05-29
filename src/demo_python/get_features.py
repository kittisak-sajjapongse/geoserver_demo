import sys

import geopandas as gpd
from owslib.wfs import WebFeatureService

# Connect to the GeoServer WFS endpoint
wfs_url = 'http://localhost:8080/geoserver/wfs'
wfs = WebFeatureService(url=wfs_url, version='1.1.0')

# List all layers
print("===== All available layers =====")
print(list(wfs.contents), end="\n\n\n")

# Load and display the features using GeoDataFrame
try:
    response = wfs.getfeature(typename='kitty:aaa', outputFormat='GML2')
    gdf = gpd.read_file(response)
    print("===== GeoDataFrame =====")
    print(gdf)
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(-1)

# Reset the io.BytesIO object
response.seek(0)
gml_data = response.read().decode("utf-8")
with open("get_features_response.xml", "w") as f:
    f.write(gml_data)



