# PresentationAlignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_object_key** | **str** |  | 
**plan_regulation_group_key** | **str** |  | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) |  | 
**rotation** | **int** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.presentation_alignment import PresentationAlignment

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationAlignment from a JSON string
presentation_alignment_instance = PresentationAlignment.from_json(json)
# print the JSON string representation of the object
print(PresentationAlignment.to_json())

# convert the object into a dict
presentation_alignment_dict = presentation_alignment_instance.to_dict()
# create an instance of PresentationAlignment from a dict
presentation_alignment_from_dict = PresentationAlignment.from_dict(presentation_alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


