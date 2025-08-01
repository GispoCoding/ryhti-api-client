# BuildingOrdinance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_building_ordinance_identifier** | **str** | Rakennusjärjestyksen pysyvä tunnus | 
**building_ordinance_uri** | **str** |  | [optional] [readonly] 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**administrative_area_identifiers** | **List[str]** | Hallinnollisen alueen tunnus (kuntanumero), jota rakennusjärjestys koskee | 
**approval_date** | **date** | Rakennusjärjestyksen hyväksymispäivämäärä | 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | Rakennusjärjestyksen voimassaoloaika | 
**attachment_documents** | [**List[BuildingOrdinanceAttachmentDocument]**](BuildingOrdinanceAttachmentDocument.md) | Rakennusjärjestys-liiteasiakirja tai siihen olennaisesti kuuluva liiteasiakirja | 

## Example

```python
from ryhti_api_client.models.building_ordinance import BuildingOrdinance

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingOrdinance from a JSON string
building_ordinance_instance = BuildingOrdinance.from_json(json)
# print the JSON string representation of the object
print(BuildingOrdinance.to_json())

# convert the object into a dict
building_ordinance_dict = building_ordinance_instance.to_dict()
# create an instance of BuildingOrdinance from a dict
building_ordinance_from_dict = BuildingOrdinance.from_dict(building_ordinance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


