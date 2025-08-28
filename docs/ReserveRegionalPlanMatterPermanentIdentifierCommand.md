# ReserveRegionalPlanMatterPermanentIdentifierCommand

Sanoma maakuntakaavojen pysyvien tunnisteiden varaamiseen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area_identifier** | **str** | Hallinnollisen alueen tunnus (esim. kunta tai maakunta) | [optional] 
**project_name** | **str** | Kaavahankkeen pysyvä nimi. Nimi on uniikki eikä sitä voi vaihtaa. | [optional] 

## Example

```python
from ryhti_api_client.models.reserve_regional_plan_matter_permanent_identifier_command import ReserveRegionalPlanMatterPermanentIdentifierCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveRegionalPlanMatterPermanentIdentifierCommand from a JSON string
reserve_regional_plan_matter_permanent_identifier_command_instance = ReserveRegionalPlanMatterPermanentIdentifierCommand.from_json(json)
# print the JSON string representation of the object
print(ReserveRegionalPlanMatterPermanentIdentifierCommand.to_json())

# convert the object into a dict
reserve_regional_plan_matter_permanent_identifier_command_dict = reserve_regional_plan_matter_permanent_identifier_command_instance.to_dict()
# create an instance of ReserveRegionalPlanMatterPermanentIdentifierCommand from a dict
reserve_regional_plan_matter_permanent_identifier_command_from_dict = ReserveRegionalPlanMatterPermanentIdentifierCommand.from_dict(reserve_regional_plan_matter_permanent_identifier_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


