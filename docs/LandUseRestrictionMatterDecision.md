# LandUseRestrictionMatterDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**land_use_restriction_matter_decision_key** | **str** | Avain | 
**land_use_restriction_matter_decision_uri** | **str** |  | [optional] [readonly] 
**decision_date** | **date** | Päätöspäivämäärä | 
**date_of_decision** | **date** | Päätöksenantopäivämäärä | 
**date_of_validity** | **date** | Lainvoimaisuuspäivämäärä | 
**decision_documents** | [**List[LandUseRestrictionAttachmentDocument]**](LandUseRestrictionAttachmentDocument.md) | Päätösasiakirjat | 
**decision_maker** | [**LandUseRestrictionOperator**](LandUseRestrictionOperator.md) | Päätöksentekijä | 
**name** | **str** | Päätöksen nimitys, joka kertoo mitä päätös koskee. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/AlueidenkayttopaatoksenNimi\&quot;&gt;http://uri.suomi.fi/codelist/rytj/AlueidenkayttopaatoksenNimi&lt;/a&gt; | 
**type_of_decision_maker** | **str** | Päättäjän laji. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija\&quot;&gt;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija&lt;/a&gt; | 
**decision_identifier** | **str** | Päätöstunnus | [optional] 
**statute** | [**Statute**](Statute.md) | Ohjaava säädös | [optional] 
**land_use_restriction** | [**LandUseRestriction**](LandUseRestriction.md) | Alueidenkäytön rajoitus | [optional] 

## Example

```python
from ryhti_api_client.models.land_use_restriction_matter_decision import LandUseRestrictionMatterDecision

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionMatterDecision from a JSON string
land_use_restriction_matter_decision_instance = LandUseRestrictionMatterDecision.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionMatterDecision.to_json())

# convert the object into a dict
land_use_restriction_matter_decision_dict = land_use_restriction_matter_decision_instance.to_dict()
# create an instance of LandUseRestrictionMatterDecision from a dict
land_use_restriction_matter_decision_from_dict = LandUseRestrictionMatterDecision.from_dict(land_use_restriction_matter_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


