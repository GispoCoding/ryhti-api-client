# PlanMap

Kaavakartta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_map_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_map_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planmap/{guid}) | [optional] [readonly] 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**file_key** | **str** |  | 
**coordinate_system** | **str** |  | 

## Example

```python
from ryhti_api_client.models.plan_map import PlanMap

# TODO update the JSON string below
json = "{}"
# create an instance of PlanMap from a JSON string
plan_map_instance = PlanMap.from_json(json)
# print the JSON string representation of the object
print(PlanMap.to_json())

# convert the object into a dict
plan_map_dict = plan_map_instance.to_dict()
# create an instance of PlanMap from a dict
plan_map_from_dict = PlanMap.from_dict(plan_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


