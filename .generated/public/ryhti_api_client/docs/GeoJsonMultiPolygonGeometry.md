# GeoJsonMultiPolygonGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;MultiPolygon\&quot; | 
**coordinates** | **List[List[List[List[float]]]]** | Koordinaatit | 

## Example

```python
from ryhti_api_client.models.geo_json_multi_polygon_geometry import GeoJsonMultiPolygonGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonMultiPolygonGeometry from a JSON string
geo_json_multi_polygon_geometry_instance = GeoJsonMultiPolygonGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonMultiPolygonGeometry.to_json())

# convert the object into a dict
geo_json_multi_polygon_geometry_dict = geo_json_multi_polygon_geometry_instance.to_dict()
# create an instance of GeoJsonMultiPolygonGeometry from a dict
geo_json_multi_polygon_geometry_from_dict = GeoJsonMultiPolygonGeometry.from_dict(geo_json_multi_polygon_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


