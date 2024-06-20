import requests

# Prerequisites:
# 1. Create the workspace, referred in this example, on GeoServer.
#       1.1. Grant write privilege for the user (admin), referred in this example, on the workspace.
#       1.2. Enable all services (i.e. WFS, WCS, WMS, WMTS) on the workspace
# 2. Setup POSTGIS store for the workspace
# 3. Create the layer, referred in this example, on the store
#       3.1. Add attribute 'the_geom' of type 'Point' to the layer
#       3.2. Add attribute 'name' of type 'String' to the layer
#       3.3. Add attribute 'description' of type 'String' to the layer
#       3.4. Grant write privilege for the user (admin), referred in this example, on the layer.
#
# Note: Access http://localhost:8080/geoserver on a browser to setup

# Connect to the GeoServer WFS endpoint
wfs_url = 'http://localhost:8080/geoserver/wfs'

headers = {'Content-Type': 'application/xml'}

# This point is located in Pataya Thailand
new_point_xml = f"""
<wfs:Transaction service="WFS" version="1.1.0"
    xmlns:wfs="http://www.opengis.net/wfs"
    xmlns:gml="http://www.opengis.net/gml"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.opengis.net/wfs
    http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">
    <wfs:Insert>
        <gis:test_point xmlns:gis="gis">
            <gis:the_geom>
                <gml:Point srsName="EPSG:4326">
                    <gml:coordinates>100.858131,12.908030</gml:coordinates>
                </gml:Point>
            </gis:the_geom>
            <gis:name>Name of point1</gis:name>
            <gis:description>Description of point1</gis:description>
        </gis:test_point>
        <gis:test_point xmlns:gis="gis">
            <gis:the_geom>
                <gml:Point srsName="EPSG:4326">
                    <gml:coordinates>101.858131,12.908030</gml:coordinates>
                </gml:Point>
            </gis:the_geom>
            <gis:name>Name of point2</gis:name>
            <gis:description>Description of point2</gis:description>
        </gis:test_point>
    </wfs:Insert>
</wfs:Transaction>
"""

response = requests.post(wfs_url, data=new_point_xml, headers=headers, auth=("admin","geoserver"))

# Print the response
print(response.text)