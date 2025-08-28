# BoundaryPoint

Rajapiste

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundary_point_or_peg_id** | **str** | Rajapisteen tai rajapyykin tunnus | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Pistegeometria (Geometriatyypin oltava GeoJsonPointGeometryGeoJsonPointGeometry) | 

## Example

```python
from ryhti_api_client.models.boundary_point import BoundaryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of BoundaryPoint from a JSON string
boundary_point_instance = BoundaryPoint.from_json(json)
# print the JSON string representation of the object
print(BoundaryPoint.to_json())

# convert the object into a dict
boundary_point_dict = boundary_point_instance.to_dict()
# create an instance of BoundaryPoint from a dict
boundary_point_from_dict = BoundaryPoint.from_dict(boundary_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


