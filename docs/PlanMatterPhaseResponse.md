# PlanMatterPhaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_matter_phase_key** | **str** |  | [optional] 
**plan_matter_phase_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planmatterphase/{guid}) | [optional] [readonly] 
**life_cycle_status** | **str** |  | [optional] 
**geographical_area** | [**RyhtiGeometry**](RyhtiGeometry.md) |  | [optional] 
**handling_event** | [**HandlingEvent**](HandlingEvent.md) | Käsittelytapahtuma | [optional] 
**interaction_events** | [**List[InteractionEvent]**](InteractionEvent.md) |  | [optional] 
**plan_decision** | [**PlanDecision**](PlanDecision.md) | Kaavapäätös | [optional] 
**previous_phase_key** | **str** |  | [optional] 
**next_phase_key** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.plan_matter_phase_response import PlanMatterPhaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanMatterPhaseResponse from a JSON string
plan_matter_phase_response_instance = PlanMatterPhaseResponse.from_json(json)
# print the JSON string representation of the object
print(PlanMatterPhaseResponse.to_json())

# convert the object into a dict
plan_matter_phase_response_dict = plan_matter_phase_response_instance.to_dict()
# create an instance of PlanMatterPhaseResponse from a dict
plan_matter_phase_response_from_dict = PlanMatterPhaseResponse.from_dict(plan_matter_phase_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


