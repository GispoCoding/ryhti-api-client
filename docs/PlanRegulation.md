# PlanRegulation

Kaavamääräys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_regulation_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_regulation_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{guid}) | [optional] [readonly] 
**value** | [**PlanRegulationValue**](PlanRegulationValue.md) |  | [optional] 
**life_cycle_status** | **str** | Kaavamääräyksen elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari&lt;/a&gt; | 
**type** | **str** | Määräys tai määräyksen osa, jolla ohjataan alueidenkäyttöä ja rakentamista. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayslaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayslaji&lt;/a&gt; | 
**verbal_regulations** | **List[str]** | Sanallisen kaavamääräyksen luokittelu. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_Sanallisen_Kaavamaarayksen_Laji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_Sanallisen_Kaavamaarayksen_Laji&lt;/a&gt; | [optional] 
**additional_informations** | [**List[AdditionalInformation]**](AdditionalInformation.md) |  | [optional] 
**related_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) |  | [optional] 
**plan_themes** | **List[str]** | Kaavamääräyksen teemoittelu. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavoitusteema\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavoitusteema&lt;/a&gt; | [optional] 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) |  | [optional] 
**subject_identifiers** | **List[str]** |  | [optional] 
**regulation_number** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.plan_regulation import PlanRegulation

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRegulation from a JSON string
plan_regulation_instance = PlanRegulation.from_json(json)
# print the JSON string representation of the object
print(PlanRegulation.to_json())

# convert the object into a dict
plan_regulation_dict = plan_regulation_instance.to_dict()
# create an instance of PlanRegulation from a dict
plan_regulation_from_dict = PlanRegulation.from_dict(plan_regulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


