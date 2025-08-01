# PlanRegulationValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Koodiston arvo (uri) | [optional] 
**code_list** | **str** | Koodisto | [optional] 
**title** | [**LanguageString**](LanguageString.md) | Nimi | [optional] 
**data_type** | **str** | Enumeraatio joka määrittää Arvo-luokkien (Domain.ValueObjects.AttributeValue) tyypin.  Jokaisella konkreettisella Arvo-luokan (Domain.ValueObjects.AttributeValue) toteutuksella tulee olla sitä vastaava DataType enumeraation arvo. | 
**number** | **int** | Arvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**minimum_value** | **float** | Minimiarvo | [optional] 
**maximum_value** | **float** | Maksimiarvo | [optional] 
**identifier** | **str** | Tunnus | [optional] 
**register_identifier** | **str** | Järjestelmän tunnus | [optional] 
**register_name** | [**LanguageString**](LanguageString.md) | Järjestelmän nimi | [optional] 
**text** | **str** | Teksti | [optional] 
**syntax** | **str** | Syntaksi | [optional] 
**begin_utc** | **datetime** | Alkuaika | [optional] 
**end_utc** | **datetime** | Loppuaika | [optional] 
**begin** | **date** | Alkupäivä | [optional] 
**end** | **date** | Loppupäivä | [optional] 

## Example

```python
from ryhti_api_client.models.plan_regulation_value import PlanRegulationValue

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRegulationValue from a JSON string
plan_regulation_value_instance = PlanRegulationValue.from_json(json)
# print the JSON string representation of the object
print(PlanRegulationValue.to_json())

# convert the object into a dict
plan_regulation_value_dict = plan_regulation_value_instance.to_dict()
# create an instance of PlanRegulationValue from a dict
plan_regulation_value_from_dict = PlanRegulationValue.from_dict(plan_regulation_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


