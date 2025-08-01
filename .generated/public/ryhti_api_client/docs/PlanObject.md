# PlanObject

Kaavakohde

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_object_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_object_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planobject/{guid}) | [optional] [readonly] 
**life_cycle_status** | **str** | Kaavakohteen elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari&lt;/a&gt; | 
**underground_status** | **str** | Luokittelu maanalaista ja maanpäällistä maankäyttöä koskeviin kaavakohteisiin. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_MaanalaisuudenLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_MaanalaisuudenLaji&lt;/a&gt; | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Geometria | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**vertical_limit** | [**DecimalRange**](DecimalRange.md) | Desimaaliarvoväli | [optional] 
**related_plan_source_data_keys** | **List[str]** | Viittaus (GUID) kaavan mukana toimitettavaan lähtötietoaineistoon sisältyvään tietokohteeseen, joka liittyy kaavakohteeseen. Esim. Pohjavesialue.  Päivitysvaiheessa tämän listan kuuluu olla tyhjä. | [optional] 
**related_plan_source_data_uris** | **List[str]** | Viittaus (URI) kaava-asian mukana toimitettavaan, aiemmin tallennettuun, lähtötietoaineistoon sisältyvään tietokohteeseen, joka liittyy tallennettuun kaavakohteeseen. Esim. Pohjavesialue. | [optional] 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | VoimassaoloAika | [optional] 
**object_number** | **int** | Kohdenumero | [optional] 
**related_plan_object_keys** | **List[str]** | LiittyväKohde UUID/localID | [optional] 

## Example

```python
from ryhti_api_client.models.plan_object import PlanObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlanObject from a JSON string
plan_object_instance = PlanObject.from_json(json)
# print the JSON string representation of the object
print(PlanObject.to_json())

# convert the object into a dict
plan_object_dict = plan_object_instance.to_dict()
# create an instance of PlanObject from a dict
plan_object_from_dict = PlanObject.from_dict(plan_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


