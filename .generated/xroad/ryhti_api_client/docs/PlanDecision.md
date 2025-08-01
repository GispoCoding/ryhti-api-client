# PlanDecision

Kaavapäätös

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_decision_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_decision_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plandecision/{guid}) | [optional] [readonly] 
**name** | **str** | Päätöksen nimitys, joka kertoo mitä päätös koskee. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavpaatnimi\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavpaatnimi&lt;/a&gt; | 
**decision_date** | **date** | Päätöspäivämäärä | 
**date_of_decision** | **date** | Päätöksenantopäivämäärä | 
**decision_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) | Päätösasiakirja | [optional] 
**decision_article** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**decision_text** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**type_of_decision_maker** | **str** | Päätöksen tekijä, monijäseninen toimielin tai viranhaltija. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija\&quot;&gt;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija&lt;/a&gt; | 
**decision_identifier** | **str** | Päätöstunnus | [optional] 
**statutes** | [**List[Statute]**](Statute.md) | Ohjaava säädös | [optional] 
**plans** | [**List[Plan]**](Plan.md) | Kaavapäätökset | [optional] 
**date_of_validity** | **date** | Lainvoimaisuuspäivämäärä | [optional] 
**decision_makers** | [**List[PlanOperator]**](PlanOperator.md) | Päätöksentekijä | [optional] 
**plan_cancellation_infos** | [**List[PlanCancellationInfo]**](PlanCancellationInfo.md) | Kumoamistieto | [optional] 

## Example

```python
from ryhti_api_client.models.plan_decision import PlanDecision

# TODO update the JSON string below
json = "{}"
# create an instance of PlanDecision from a JSON string
plan_decision_instance = PlanDecision.from_json(json)
# print the JSON string representation of the object
print(PlanDecision.to_json())

# convert the object into a dict
plan_decision_dict = plan_decision_instance.to_dict()
# create an instance of PlanDecision from a dict
plan_decision_from_dict = PlanDecision.from_dict(plan_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


