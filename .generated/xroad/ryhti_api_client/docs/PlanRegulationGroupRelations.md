# PlanRegulationGroupRelations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_object_key** | **str** |  | [optional] 
**plan_regulation_group_key** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.plan_regulation_group_relations import PlanRegulationGroupRelations

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRegulationGroupRelations from a JSON string
plan_regulation_group_relations_instance = PlanRegulationGroupRelations.from_json(json)
# print the JSON string representation of the object
print(PlanRegulationGroupRelations.to_json())

# convert the object into a dict
plan_regulation_group_relations_dict = plan_regulation_group_relations_instance.to_dict()
# create an instance of PlanRegulationGroupRelations from a dict
plan_regulation_group_relations_from_dict = PlanRegulationGroupRelations.from_dict(plan_regulation_group_relations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


