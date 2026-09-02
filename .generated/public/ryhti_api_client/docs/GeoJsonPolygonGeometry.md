# GeoJsonPolygonGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;Polygon\&quot; | 
**coordinates** | **List[List[List[float]]]** | Koordinaatit | 

## Example

```python
from ryhti_api_client.models.geo_json_polygon_geometry import GeoJsonPolygonGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPolygonGeometry from a JSON string
geo_json_polygon_geometry_instance = GeoJsonPolygonGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPolygonGeometry.to_json())

# convert the object into a dict
geo_json_polygon_geometry_dict = geo_json_polygon_geometry_instance.to_dict()
# create an instance of GeoJsonPolygonGeometry from a dict
geo_json_polygon_geometry_from_dict = GeoJsonPolygonGeometry.from_dict(geo_json_polygon_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


