# PlanRecommendation

Kaavasuositus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_recommendation_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_recommendation_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planrecommendation/{guid}) | [optional] [readonly] 
**value** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**life_cycle_status** | **str** | Kaavasuosituksen elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari&lt;/a&gt; | 
**related_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) | LiittyväAsiakirja | [optional] 
**plan_themes** | **List[str]** | Kaavasuosituksen teemoittelu. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavoitusteema\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavoitusteema&lt;/a&gt; | [optional] 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | VoimassaoloAika | [optional] 
**recommendation_number** | **int** | Suositusnumero | [optional] 

## Example

```python
from ryhti_api_client.models.plan_recommendation import PlanRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRecommendation from a JSON string
plan_recommendation_instance = PlanRecommendation.from_json(json)
# print the JSON string representation of the object
print(PlanRecommendation.to_json())

# convert the object into a dict
plan_recommendation_dict = plan_recommendation_instance.to_dict()
# create an instance of PlanRecommendation from a dict
plan_recommendation_from_dict = PlanRecommendation.from_dict(plan_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


