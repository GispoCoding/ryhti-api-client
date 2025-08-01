# RyhtiGeometryGeometry

Geometria GeoJson rakenteella: https://geojson.org/

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[List[List[List[float]]]]** | Koordinaatit | 
**type** | **str** | Tuetut geometriatyypit | 

## Example

```python
from ryhti_api_client.models.ryhti_geometry_geometry import RyhtiGeometryGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of RyhtiGeometryGeometry from a JSON string
ryhti_geometry_geometry_instance = RyhtiGeometryGeometry.from_json(json)
# print the JSON string representation of the object
print(RyhtiGeometryGeometry.to_json())

# convert the object into a dict
ryhti_geometry_geometry_dict = ryhti_geometry_geometry_instance.to_dict()
# create an instance of RyhtiGeometryGeometry from a dict
ryhti_geometry_geometry_from_dict = RyhtiGeometryGeometry.from_dict(ryhti_geometry_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


