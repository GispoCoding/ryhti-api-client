# RelatedRegulationGroupPlanObjectRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_regulation_group_uri** | **str** | Liittyvän määräysryhmän uri | [optional] [readonly] 
**plan_object_key** | **str** | Sisäisen kaavakohteen avain | [optional] [readonly] 

## Example

```python
from ryhti_api_client.models.related_regulation_group_plan_object_relation import RelatedRegulationGroupPlanObjectRelation

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedRegulationGroupPlanObjectRelation from a JSON string
related_regulation_group_plan_object_relation_instance = RelatedRegulationGroupPlanObjectRelation.from_json(json)
# print the JSON string representation of the object
print(RelatedRegulationGroupPlanObjectRelation.to_json())

# convert the object into a dict
related_regulation_group_plan_object_relation_dict = related_regulation_group_plan_object_relation_instance.to_dict()
# create an instance of RelatedRegulationGroupPlanObjectRelation from a dict
related_regulation_group_plan_object_relation_from_dict = RelatedRegulationGroupPlanObjectRelation.from_dict(related_regulation_group_plan_object_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


