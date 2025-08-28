# ReservePermanentLandUseRestrictionIdentifierCommand

Sanoma alueidenkäytön rajoitusten pysyvien tunnisteiden varaamiseen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area_identifier** | **str** | Hallinnollisen alueen tunnus (esim. kunta tai maakunta) | [optional] 
**project_name** | **str** | Kaavahankkeen pysyvä nimi. Nimi on uniikki eikä sitä voi vaihtaa. | [optional] 

## Example

```python
from ryhti_api_client.models.reserve_permanent_land_use_restriction_identifier_command import ReservePermanentLandUseRestrictionIdentifierCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReservePermanentLandUseRestrictionIdentifierCommand from a JSON string
reserve_permanent_land_use_restriction_identifier_command_instance = ReservePermanentLandUseRestrictionIdentifierCommand.from_json(json)
# print the JSON string representation of the object
print(ReservePermanentLandUseRestrictionIdentifierCommand.to_json())

# convert the object into a dict
reserve_permanent_land_use_restriction_identifier_command_dict = reserve_permanent_land_use_restriction_identifier_command_instance.to_dict()
# create an instance of ReservePermanentLandUseRestrictionIdentifierCommand from a dict
reserve_permanent_land_use_restriction_identifier_command_from_dict = ReservePermanentLandUseRestrictionIdentifierCommand.from_dict(reserve_permanent_land_use_restriction_identifier_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


