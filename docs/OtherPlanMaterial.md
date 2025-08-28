# OtherPlanMaterial

MuuKaavaAineisto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other_plan_material_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**other_plan_material_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/otherplanmaterial/{guid}) | [optional] [readonly] 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**file_key** | **str** | Tiedosto | [optional] 
**other_plan_material_link** | **str** | MuuKaavaAineistoLinkki | [optional] 
**personal_data_content** | **str** | Kuvaa muun kaava-aineiston henkilötietosisällön. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/henkilotietosisalto\&quot;&gt;http://uri.suomi.fi/codelist/rytj/henkilotietosisalto&lt;/a&gt; | 
**category_of_publicity** | **str** | Kuvaa muun kaava-aineiston julkisuusluokan. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/julkisuus\&quot;&gt;http://uri.suomi.fi/codelist/rytj/julkisuus&lt;/a&gt; | 

## Example

```python
from ryhti_api_client.models.other_plan_material import OtherPlanMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of OtherPlanMaterial from a JSON string
other_plan_material_instance = OtherPlanMaterial.from_json(json)
# print the JSON string representation of the object
print(OtherPlanMaterial.to_json())

# convert the object into a dict
other_plan_material_dict = other_plan_material_instance.to_dict()
# create an instance of OtherPlanMaterial from a dict
other_plan_material_from_dict = OtherPlanMaterial.from_dict(other_plan_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


