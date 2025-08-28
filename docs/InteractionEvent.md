# InteractionEvent

Vuorovaikutustapahtuma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_event_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**interaction_event_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/interactionevent/{guid}) | [optional] [readonly] 
**interaction_event_type** | **str** | Vuorovaikutustapahtuman tyyppi. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_KaavanVuorovaikutustapahtumanLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_KaavanVuorovaikutustapahtumanLaji&lt;/a&gt; | 
**event_time** | [**TimePeriod**](TimePeriod.md) |  | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**location** | [**RyhtiGeometry**](RyhtiGeometry.md) |  | [optional] 
**additional_information_link** | **str** | Lisätietolinkki | [optional] 
**cancelled** | **bool** | Peruttu | [optional] 
**related_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) | Liittyvät asiakirjat | [optional] 

## Example

```python
from ryhti_api_client.models.interaction_event import InteractionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionEvent from a JSON string
interaction_event_instance = InteractionEvent.from_json(json)
# print the JSON string representation of the object
print(InteractionEvent.to_json())

# convert the object into a dict
interaction_event_dict = interaction_event_instance.to_dict()
# create an instance of InteractionEvent from a dict
interaction_event_from_dict = InteractionEvent.from_dict(interaction_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


