import requests

# Prerequisites:
# 1. Create the workspace, referred in this example, on GeoServer.
#       1.1. Grant write privilege for the user (admin), referred in this example, on the workspace.
#       1.2. Enable all services (i.e. WFS, WCS, WMS, WMTS) on the workspace
# 2. Setup POSTGIS store for the workspace
# 3. Create the layer, referred in this example, on the store
#       3.1. Add attribute 'the_geom' of type 'MultiPolygon' to the layer
#       3.2. Add attribute 'name' of type 'String' to the layer
#       3.3. Grant write privilege for the user (admin), referred in this example, on the layer.
#
# Note: Access http://localhost:8080/geoserver on a browser to setup


# Connect to the GeoServer WFS endpoint
wfs_url = 'http://localhost:8080/geoserver/wfs'

# Construct the XML for the WFS-T insert request
# This example assumes you want to insert a new point feature

headers = {'Content-Type': 'application/xml'}

# This polygon is located in Bangkok Thailand
new_feature_xml = f"""
<wfs:Transaction service="WFS" version="1.1.0"
    xmlns:wfs="http://www.opengis.net/wfs"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:gml="http://www.opengis.net/gml"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.opengis.net/wfs
                        http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">
  <wfs:Insert>
    <kitty:aaa xmlns:kitty="kitty">
      <kitty:the_geom>
        <gml:MultiSurface srsName="urn:x-ogc:def:crs:EPSG:4326" srsDimension="2">
            <gml:surfaceMember>
                <gml:Polygon>
                    <gml:exterior>
                        <gml:LinearRing>
                            <gml:posList>13.82972439 100.61503043 13.82947755 100.61690762 13.82853768 100.61684896 13.82849971 100.6170445 13.82831933 100.61700539 13.82831933 100.61618412 13.82722755 100.61624278 13.82623071 100.61625256 13.82627818 100.61763112 13.82511045 100.61757246 13.82500602 100.61528463 13.82493007 100.61353454 13.82568008 100.61349543 13.82608831 100.61358343 13.82621173 100.61379852 13.82620223 100.61434604 13.82624021 100.6149131 13.82765477 100.61496199 13.82888895 100.61497177 13.82959148 100.61498154 13.82974337 100.61499132 13.82972439 100.61503043</gml:posList>
                        </gml:LinearRing>
                    </gml:exterior>
                </gml:Polygon>
            </gml:surfaceMember>
        </gml:MultiSurface>
      </kitty:the_geom>
      <kitty:name>Nice place</kitty:name>
    </kitty:aaa>
  </wfs:Insert>
</wfs:Transaction>
"""

response = requests.post(wfs_url, data=new_feature_xml, headers=headers, auth=("admin","geoserver"))

# Print the response
print(response.text)
