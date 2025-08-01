# RelatedPlanObjectRegulationGroupRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_plan_object_uri** | **str** | Liittyvän kaavakohteen uri | 
**regulation_group_key** | **str** | Sisäinen määräysryhmän avain | 

## Example

```python
from ryhti_api_client.models.related_plan_object_regulation_group_relation import RelatedPlanObjectRegulationGroupRelation

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedPlanObjectRegulationGroupRelation from a JSON string
related_plan_object_regulation_group_relation_instance = RelatedPlanObjectRegulationGroupRelation.from_json(json)
# print the JSON string representation of the object
print(RelatedPlanObjectRegulationGroupRelation.to_json())

# convert the object into a dict
related_plan_object_regulation_group_relation_dict = related_plan_object_regulation_group_relation_instance.to_dict()
# create an instance of RelatedPlanObjectRegulationGroupRelation from a dict
related_plan_object_regulation_group_relation_from_dict = RelatedPlanObjectRegulationGroupRelation.from_dict(related_plan_object_regulation_group_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


