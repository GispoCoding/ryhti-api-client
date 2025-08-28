# GeoJsonLineStringGeometry

LineString GeoJson    Esimerkki: { \"type\": \"lineString\", \"coordinates\": [ [100.0, 0.0], [101.0, 1.0] ] }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[List[float]]** | Koordinaatit | 
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;lineString\&quot; | 

## Example

```python
from ryhti_api_client.models.geo_json_line_string_geometry import GeoJsonLineStringGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonLineStringGeometry from a JSON string
geo_json_line_string_geometry_instance = GeoJsonLineStringGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonLineStringGeometry.to_json())

# convert the object into a dict
geo_json_line_string_geometry_dict = geo_json_line_string_geometry_instance.to_dict()
# create an instance of GeoJsonLineStringGeometry from a dict
geo_json_line_string_geometry_from_dict = GeoJsonLineStringGeometry.from_dict(geo_json_line_string_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


