# GeoJsonMultiPointGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Geometriatyyppi. Pakollinen arvo: \&quot;MultiPoint\&quot; | 
**coordinates** | **List[List[float]]** | Koordinaatit | 

## Example

```python
from ryhti_api_client.models.geo_json_multi_point_geometry import GeoJsonMultiPointGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonMultiPointGeometry from a JSON string
geo_json_multi_point_geometry_instance = GeoJsonMultiPointGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonMultiPointGeometry.to_json())

# convert the object into a dict
geo_json_multi_point_geometry_dict = geo_json_multi_point_geometry_instance.to_dict()
# create an instance of GeoJsonMultiPointGeometry from a dict
geo_json_multi_point_geometry_from_dict = GeoJsonMultiPointGeometry.from_dict(geo_json_multi_point_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


