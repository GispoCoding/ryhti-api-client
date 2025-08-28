# BuildingOrdinanceOperator

Toimija

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building_ordinance_operator_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**building_ordinance_operator_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/buildingordinanceoperator/{guid}) | [optional] [readonly] 
**first_name** | **str** | Toimijan etunimi | [optional] 
**last_name** | **str** | Toimijan sukunimi | [optional] 
**title** | **str** | Toimijan nimike | [optional] 
**organization_name** | **str** | Toimijan organisaation nimi | [optional] 
**business_id** | **str** | Toimijan organisaation y-tunnus | [optional] 

## Example

```python
from ryhti_api_client.models.building_ordinance_operator import BuildingOrdinanceOperator

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingOrdinanceOperator from a JSON string
building_ordinance_operator_instance = BuildingOrdinanceOperator.from_json(json)
# print the JSON string representation of the object
print(BuildingOrdinanceOperator.to_json())

# convert the object into a dict
building_ordinance_operator_dict = building_ordinance_operator_instance.to_dict()
# create an instance of BuildingOrdinanceOperator from a dict
building_ordinance_operator_from_dict = BuildingOrdinanceOperator.from_dict(building_ordinance_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


