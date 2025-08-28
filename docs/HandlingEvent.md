# HandlingEvent

Käsittelytapahtuma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handling_event_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**handling_event_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/handlingevent/{guid}) | [optional] [readonly] 
**handling_event_type** | **str** | Käsittelytapahtuman tyyppi. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavakastap\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavakastap&lt;/a&gt; | 
**event_time** | **date** |  | [optional] 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**location** | [**RyhtiGeometry**](RyhtiGeometry.md) | Käsittelytapahtuman sijainti | [optional] 
**additional_information_link** | **str** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**related_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) |  | [optional] 

## Example

```python
from ryhti_api_client.models.handling_event import HandlingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HandlingEvent from a JSON string
handling_event_instance = HandlingEvent.from_json(json)
# print the JSON string representation of the object
print(HandlingEvent.to_json())

# convert the object into a dict
handling_event_dict = handling_event_instance.to_dict()
# create an instance of HandlingEvent from a dict
handling_event_from_dict = HandlingEvent.from_dict(handling_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


