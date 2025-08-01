# ReserveLocalDetailedPlanMatterPermanentIdentifierCommand

Sanoma asemakaavojen pysyvien tunnisteiden varaamiseen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area_identifier** | **str** | Hallinnollisen alueen tunnus (esim. kunta tai maakunta) | [optional] 
**project_name** | **str** | Kaavahankkeen pysyvä nimi. Nimi on uniikki eikä sitä voi vaihtaa. | [optional] 

## Example

```python
from ryhti_api_client.models.reserve_local_detailed_plan_matter_permanent_identifier_command import ReserveLocalDetailedPlanMatterPermanentIdentifierCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveLocalDetailedPlanMatterPermanentIdentifierCommand from a JSON string
reserve_local_detailed_plan_matter_permanent_identifier_command_instance = ReserveLocalDetailedPlanMatterPermanentIdentifierCommand.from_json(json)
# print the JSON string representation of the object
print(ReserveLocalDetailedPlanMatterPermanentIdentifierCommand.to_json())

# convert the object into a dict
reserve_local_detailed_plan_matter_permanent_identifier_command_dict = reserve_local_detailed_plan_matter_permanent_identifier_command_instance.to_dict()
# create an instance of ReserveLocalDetailedPlanMatterPermanentIdentifierCommand from a dict
reserve_local_detailed_plan_matter_permanent_identifier_command_from_dict = ReserveLocalDetailedPlanMatterPermanentIdentifierCommand.from_dict(reserve_local_detailed_plan_matter_permanent_identifier_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


