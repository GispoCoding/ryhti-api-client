# LandUseRestrictionMatterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_land_use_restriction_identifier** | **str** | Alueidenkäytön rajoituksen pysyvä tunnus | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**land_use_restriction_type** | **str** | Alueidenkäytön rajoituksen tyyppi. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenLaji&lt;/a&gt; | 
**time_of_initiation** | **date** | Vireilletulopäivämäärä | 
**administrative_area_identifiers** | **List[str]** | hallinnollisen alueen tunnukset | 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**case_identifiers** | **List[str]** | Asianhallintatunnukset | [optional] 
**record_numbers** | **List[str]** | Diaarinumerot | [optional] 
**producer_land_use_restriction_identifier** | **str** | Kunnan antama alueidenkäytön rajoituksen tunnus | [optional] 
**matter_annexes** | [**List[LandUseRestrictionAttachmentDocument]**](LandUseRestrictionAttachmentDocument.md) | AsianLiitteet | [optional] 
**responsible_party** | [**LandUseRestrictionOperator**](LandUseRestrictionOperator.md) | Vastuutaho | [optional] 
**related_land_use_restriction_matters** | **List[str]** | Liittyvät alueidenkäytön rajoituksen asiat | [optional] 
**land_use_restriction_matter_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/landuserestrictionmatter/{identifier}) | [optional] [readonly] 
**phases** | [**List[LandUseRestrictionMatterPhase]**](LandUseRestrictionMatterPhase.md) | Vaiheet | 

## Example

```python
from ryhti_api_client.models.land_use_restriction_matter_response import LandUseRestrictionMatterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionMatterResponse from a JSON string
land_use_restriction_matter_response_instance = LandUseRestrictionMatterResponse.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionMatterResponse.to_json())

# convert the object into a dict
land_use_restriction_matter_response_dict = land_use_restriction_matter_response_instance.to_dict()
# create an instance of LandUseRestrictionMatterResponse from a dict
land_use_restriction_matter_response_from_dict = LandUseRestrictionMatterResponse.from_dict(land_use_restriction_matter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


