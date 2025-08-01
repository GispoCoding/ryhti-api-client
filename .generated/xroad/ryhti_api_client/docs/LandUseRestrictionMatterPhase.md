# LandUseRestrictionMatterPhase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**land_use_restriction_matter_phase_key** | **str** | Avain | 
**land_use_restriction_matter_phase_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/landuserestrictionmatterphase/{guid}) | [optional] [readonly] 
**life_cycle_status** | **str** | Elinkaaritila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenElinkaarenTila\&quot;&gt;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenElinkaarenTila&lt;/a&gt; | 
**handling_event** | [**LandUseRestrictionHandlingEvent**](LandUseRestrictionHandlingEvent.md) | Käsittelytapahtuma | 
**decision** | [**LandUseRestrictionMatterDecision**](LandUseRestrictionMatterDecision.md) | Päätös | 

## Example

```python
from ryhti_api_client.models.land_use_restriction_matter_phase import LandUseRestrictionMatterPhase

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionMatterPhase from a JSON string
land_use_restriction_matter_phase_instance = LandUseRestrictionMatterPhase.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionMatterPhase.to_json())

# convert the object into a dict
land_use_restriction_matter_phase_dict = land_use_restriction_matter_phase_instance.to_dict()
# create an instance of LandUseRestrictionMatterPhase from a dict
land_use_restriction_matter_phase_from_dict = LandUseRestrictionMatterPhase.from_dict(land_use_restriction_matter_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


