# ReserveBuildingOrdinancePermanentIdentifierCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area_identifier** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.reserve_building_ordinance_permanent_identifier_command import ReserveBuildingOrdinancePermanentIdentifierCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveBuildingOrdinancePermanentIdentifierCommand from a JSON string
reserve_building_ordinance_permanent_identifier_command_instance = ReserveBuildingOrdinancePermanentIdentifierCommand.from_json(json)
# print the JSON string representation of the object
print(ReserveBuildingOrdinancePermanentIdentifierCommand.to_json())

# convert the object into a dict
reserve_building_ordinance_permanent_identifier_command_dict = reserve_building_ordinance_permanent_identifier_command_instance.to_dict()
# create an instance of ReserveBuildingOrdinancePermanentIdentifierCommand from a dict
reserve_building_ordinance_permanent_identifier_command_from_dict = ReserveBuildingOrdinancePermanentIdentifierCommand.from_dict(reserve_building_ordinance_permanent_identifier_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


