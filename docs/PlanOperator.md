# PlanOperator

Toimija

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_operator_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_operator_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planoperator/{guid}) | [optional] [readonly] 
**first_name** | **str** | Etunimi | [optional] 
**last_name** | **str** | Sukunimi | [optional] 
**title** | **str** | Nimike | [optional] 
**organization_name** | **str** | OrganisaatioNimi | [optional] 
**business_id** | **str** | Y-tunnus | [optional] 

## Example

```python
from ryhti_api_client.models.plan_operator import PlanOperator

# TODO update the JSON string below
json = "{}"
# create an instance of PlanOperator from a JSON string
plan_operator_instance = PlanOperator.from_json(json)
# print the JSON string representation of the object
print(PlanOperator.to_json())

# convert the object into a dict
plan_operator_dict = plan_operator_instance.to_dict()
# create an instance of PlanOperator from a dict
plan_operator_from_dict = PlanOperator.from_dict(plan_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


