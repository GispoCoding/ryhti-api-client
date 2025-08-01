# GeneralRegulationGroup

Yleiskaavamääräysryhmä

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_regulation_group_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**general_regulation_group_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/generalregulationgroup/{guid}) | [optional] [readonly] 
**title_of_plan_regulation** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**plan_regulations** | [**List[PlanRegulation]**](PlanRegulation.md) | Kaavamääräykset | [optional] 
**plan_recommendations** | [**List[PlanRecommendation]**](PlanRecommendation.md) | Kaavasuositukset | [optional] 
**group_number** | **int** | Ryhmänumero | [optional] 

## Example

```python
from ryhti_api_client.models.general_regulation_group import GeneralRegulationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralRegulationGroup from a JSON string
general_regulation_group_instance = GeneralRegulationGroup.from_json(json)
# print the JSON string representation of the object
print(GeneralRegulationGroup.to_json())

# convert the object into a dict
general_regulation_group_dict = general_regulation_group_instance.to_dict()
# create an instance of GeneralRegulationGroup from a dict
general_regulation_group_from_dict = GeneralRegulationGroup.from_dict(general_regulation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


