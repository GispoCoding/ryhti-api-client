# PlanSourceData

Lähtötietoaineisto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_source_data_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_source_data_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plansourcedata/{guid}) | [optional] [readonly] 
**type** | **str** | Aineiston tyyppi. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_LahtotietoaineistonLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_LahtotietoaineistonLaji&lt;/a&gt; | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**geographical_area** | [**RyhtiGeometry**](RyhtiGeometry.md) | Aluerajaus | [optional] 
**additional_information_link** | **str** |  | [optional] 
**files** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) |  | [optional] 

## Example

```python
from ryhti_api_client.models.plan_source_data import PlanSourceData

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSourceData from a JSON string
plan_source_data_instance = PlanSourceData.from_json(json)
# print the JSON string representation of the object
print(PlanSourceData.to_json())

# convert the object into a dict
plan_source_data_dict = plan_source_data_instance.to_dict()
# create an instance of PlanSourceData from a dict
plan_source_data_from_dict = PlanSourceData.from_dict(plan_source_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


