# PlanEffects

Kaavan vaikutukset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_in_accordance_with_plan** | **bool** | Onko kaavan mukainen | 
**binding_plot_division_permanent_identifier** | **str** | Tonttijaon tunniste | 
**permanent_plan_identifier** | **str** | Kaavan pysyvä tunniste | 
**plan_effects_plots** | [**List[PlanEffectsPlot]**](PlanEffectsPlot.md) | Kaavan vaikutukset tonttijakotonttikohtaisesti | [optional] 

## Example

```python
from ryhti_api_client.models.plan_effects import PlanEffects

# TODO update the JSON string below
json = "{}"
# create an instance of PlanEffects from a JSON string
plan_effects_instance = PlanEffects.from_json(json)
# print the JSON string representation of the object
print(PlanEffects.to_json())

# convert the object into a dict
plan_effects_dict = plan_effects_instance.to_dict()
# create an instance of PlanEffects from a dict
plan_effects_from_dict = PlanEffects.from_dict(plan_effects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


