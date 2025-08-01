# SpotElevation

Korkeuspiste

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Arvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;spotElevation\&quot; | 

## Example

```python
from ryhti_api_client.models.spot_elevation import SpotElevation

# TODO update the JSON string below
json = "{}"
# create an instance of SpotElevation from a JSON string
spot_elevation_instance = SpotElevation.from_json(json)
# print the JSON string representation of the object
print(SpotElevation.to_json())

# convert the object into a dict
spot_elevation_dict = spot_elevation_instance.to_dict()
# create an instance of SpotElevation from a dict
spot_elevation_from_dict = SpotElevation.from_dict(spot_elevation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


