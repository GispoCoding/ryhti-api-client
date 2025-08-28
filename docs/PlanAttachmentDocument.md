# PlanAttachmentDocument

Liiteasiakirja

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_document_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**document_identifier** | **str** | Asiakirjan pysyvä tunnus, esim. diaarinumero tai muu dokumentinhallinnan tunnus. | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**personal_data_content** | **str** | Kuvaa asiakirjan henkilötietosisällön. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/henkilotietosisalto\&quot;&gt;http://uri.suomi.fi/codelist/rytj/henkilotietosisalto&lt;/a&gt; | 
**category_of_publicity** | **str** | Kuvaa asiakirjan julkisuusluokan. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/julkisuus\&quot;&gt;http://uri.suomi.fi/codelist/rytj/julkisuus&lt;/a&gt; | 
**accessibility** | **bool** |  | 
**retention_time** | **str** | Asiakirjan säilytysaika vuosina ennen sen hävittämistä. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/sailytysaika\&quot;&gt;http://uri.suomi.fi/codelist/rytj/sailytysaika&lt;/a&gt; | 
**confirmation_date** | **date** |  | [optional] 
**languages** | **List[str]** | Asiakirjan kieli tai sisältämät kielet. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/ryhtikielet\&quot;&gt;http://uri.suomi.fi/codelist/rytj/ryhtikielet&lt;/a&gt; | 
**file_key** | **str** | Erillisen rajapinnan kautta tallennetun tiedoston avain. | 
**descriptors** | [**List[Descriptor]**](Descriptor.md) |  | [optional] 
**document_date** | **date** |  | 
**arrived_date** | **date** |  | [optional] 
**plan_attachment_document_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planattachmentdocument/{guid}) | [optional] [readonly] 
**type_of_attachment** | **str** | Tieto, joka kuvaa tuotettavan asiakirjan lajia. Asiakirjoja tuotetaan yleensä asiankäsittelyyn liittyvissä yksittäisissä toimissa tai tapahtumissa (toimenpide).  Asiakirjatyyppi noudattaa yhteistä luokitusta/koodistoa, esimerkkejä arvoille ovat raportti, päätös, ilmoitus, muistio, tiedote...  Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK&lt;/a&gt; | 
**document_specification** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**document_creator_operators** | [**List[PlanOperator]**](PlanOperator.md) |  | [optional] 
**related_plan_attachment_documents** | **List[str]** | Liittyvät asiakirjat | [optional] 

## Example

```python
from ryhti_api_client.models.plan_attachment_document import PlanAttachmentDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAttachmentDocument from a JSON string
plan_attachment_document_instance = PlanAttachmentDocument.from_json(json)
# print the JSON string representation of the object
print(PlanAttachmentDocument.to_json())

# convert the object into a dict
plan_attachment_document_dict = plan_attachment_document_instance.to_dict()
# create an instance of PlanAttachmentDocument from a dict
plan_attachment_document_from_dict = PlanAttachmentDocument.from_dict(plan_attachment_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


