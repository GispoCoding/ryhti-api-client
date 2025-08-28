# RelatedPlan

Liittyvä kaava

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_plan_uri** | **str** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/plan/{plankey}) tonttijakotontin alueelle kohdistuvaan vaikuttavaan kaavaan. | [optional] 
**related_producer_plan_identifier** | **str** | Alueelle kohdistuvan vaikuttavan kaavan tuottajan kaavatunnus. | [optional] 

## Example

```python
from ryhti_api_client.models.related_plan import RelatedPlan

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedPlan from a JSON string
related_plan_instance = RelatedPlan.from_json(json)
# print the JSON string representation of the object
print(RelatedPlan.to_json())

# convert the object into a dict
related_plan_dict = related_plan_instance.to_dict()
# create an instance of RelatedPlan from a dict
related_plan_from_dict = RelatedPlan.from_dict(related_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


