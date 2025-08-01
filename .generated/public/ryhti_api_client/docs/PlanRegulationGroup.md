# PlanRegulationGroup

Kaavamääräysryhmä

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_regulation_group_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_regulation_group_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planregulationgroup/{guid}) | [optional] [readonly] 
**title_of_plan_regulation** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**letter_identifier** | **str** | KirjainTunnus | [optional] 
**plan_regulations** | [**List[PlanRegulation]**](PlanRegulation.md) | Kaavamääräykset | 
**plan_recommendations** | [**List[PlanRecommendation]**](PlanRecommendation.md) | Kaavasuositukset | [optional] 
**color_number** | **str** | Värikoodi | [optional] 
**group_number** | **int** | Ryhmänumero | [optional] 

## Example

```python
from ryhti_api_client.models.plan_regulation_group import PlanRegulationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRegulationGroup from a JSON string
plan_regulation_group_instance = PlanRegulationGroup.from_json(json)
# print the JSON string representation of the object
print(PlanRegulationGroup.to_json())

# convert the object into a dict
plan_regulation_group_dict = plan_regulation_group_instance.to_dict()
# create an instance of PlanRegulationGroup from a dict
plan_regulation_group_from_dict = PlanRegulationGroup.from_dict(plan_regulation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


