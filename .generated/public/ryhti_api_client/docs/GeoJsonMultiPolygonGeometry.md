# GeoJsonMultiPolygonGeometry

MultiPolygon GeoJson    Esimerkki: { \"type\": \"multiPolygon\", \"coordinates\": [ [ [ [102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0 ] ] ], [ [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ] ] ] }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[List[List[List[float]]]]** | Koordinaatit | 
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;multiPolygon\&quot; | 

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


