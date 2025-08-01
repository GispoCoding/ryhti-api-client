# GeoJsonPointGeometry

Point GeoJson    Esimerkki: { \"type\": \"point\", \"coordinates\": [100.0, 0.0] }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** | Koordinaatit | 
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;point\&quot; | 

## Example

```python
from ryhti_api_client.models.geo_json_point_geometry import GeoJsonPointGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointGeometry from a JSON string
geo_json_point_geometry_instance = GeoJsonPointGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointGeometry.to_json())

# convert the object into a dict
geo_json_point_geometry_dict = geo_json_point_geometry_instance.to_dict()
# create an instance of GeoJsonPointGeometry from a dict
geo_json_point_geometry_from_dict = GeoJsonPointGeometry.from_dict(geo_json_point_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


