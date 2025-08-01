# LandUseRestrictionHandlingEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handling_event_key** | **str** | Avain | 
**handling_event_uri** | **str** |  | [optional] [readonly] 
**type** | **str** | Laji. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenKasittelytapahtumanLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/alueidenkaytonRajoituksenKasittelytapahtumanLaji&lt;/a&gt; | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**event_time** | [**TimePeriod**](TimePeriod.md) | Tapahtuman aika (hetki tai aikaväli) | [optional] 

## Example

```python
from ryhti_api_client.models.land_use_restriction_handling_event import LandUseRestrictionHandlingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionHandlingEvent from a JSON string
land_use_restriction_handling_event_instance = LandUseRestrictionHandlingEvent.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionHandlingEvent.to_json())

# convert the object into a dict
land_use_restriction_handling_event_dict = land_use_restriction_handling_event_instance.to_dict()
# create an instance of LandUseRestrictionHandlingEvent from a dict
land_use_restriction_handling_event_from_dict = LandUseRestrictionHandlingEvent.from_dict(land_use_restriction_handling_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


