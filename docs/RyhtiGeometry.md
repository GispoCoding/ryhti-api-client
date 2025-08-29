# RyhtiGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**srid** | **str** | Gauss Krüger projektio; SRID koodi; SRID nimi       19;3873;ETRS89 / GK19FIN EPSG:3873       20;3874;ETRS89 / GK20FIN EPSG:3874       21;3875;ETRS89 / GK21FIN EPSG:3875       22;3876;ETRS89 / GK22FIN EPSG:3876       23;3877;ETRS89 / GK23FIN EPSG:3877       24;3878;ETRS89 / GK24FIN EPSG:3878       25;3879;ETRS89 / GK25FIN EPSG:3879       26;3880;ETRS89 / GK26FIN EPSG:3880       27;3881;ETRS89 / GK27FIN EPSG:3881       28;3882;ETRS89 / GK28FIN EPSG:3882       29;3883;ETRS89 / GK29FIN EPSG:3883       30;3884;ETRS89 / GK30FIN EPSG:3884       31;3885;ETRS89 / GK31FIN EPSG:3885       3067 TM35FIN   | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) |  | 

## Example

```python
from ryhti_api_client.models.ryhti_geometry import RyhtiGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of RyhtiGeometry from a JSON string
ryhti_geometry_instance = RyhtiGeometry.from_json(json)
# print the JSON string representation of the object
print(RyhtiGeometry.to_json())

# convert the object into a dict
ryhti_geometry_dict = ryhti_geometry_instance.to_dict()
# create an instance of RyhtiGeometry from a dict
ryhti_geometry_from_dict = RyhtiGeometry.from_dict(ryhti_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


