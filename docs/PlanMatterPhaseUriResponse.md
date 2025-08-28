# PlanMatterPhaseUriResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_matter_phase_key** | **str** |  | [optional] 
**plan_matter_phase_uri** | **str** |  | [optional] 
**life_cycle_status** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.plan_matter_phase_uri_response import PlanMatterPhaseUriResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanMatterPhaseUriResponse from a JSON string
plan_matter_phase_uri_response_instance = PlanMatterPhaseUriResponse.from_json(json)
# print the JSON string representation of the object
print(PlanMatterPhaseUriResponse.to_json())

# convert the object into a dict
plan_matter_phase_uri_response_dict = plan_matter_phase_uri_response_instance.to_dict()
# create an instance of PlanMatterPhaseUriResponse from a dict
plan_matter_phase_uri_response_from_dict = PlanMatterPhaseUriResponse.from_dict(plan_matter_phase_uri_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


