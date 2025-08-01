# PlanMatterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_plan_identifier** | **str** | pysyväKaavaTunnus Esim AK-00001 | 
**plan_type** | **str** | Kaavan tyyppi. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji&lt;/a&gt; | 
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**time_of_initiation** | **date** | vireilletulopäivämäärä | 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**producer_plan_identifier** | **str** | kunnan tai maakunnan tuottajakohtainen kaavatunnus | [optional] 
**case_identifiers** | **List[str]** | asianhallintatunnukset | [optional] 
**related_binding_plot_division_matter_uri** | **str** | Deprecated, use relatedBindingPlotDivisionMatterUris | [optional] 
**related_binding_plot_division_matter_uris** | **List[str]** | Liittyvät pysyvät tonttijakoasiat (URI) | [optional] 
**record_numbers** | **List[str]** | diaarinumerot | [optional] 
**administrative_area_identifiers** | **List[str]** | Hallinnollisen alueen tunnus. Kuntatunnus tai maakuntatunnus. | 
**digital_origin** | **str** | Tieto kaavan digitaalisen muodon tuotantotavasta ja siihen liittyvästä juridisuuden asteesta. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_DigitaalinenAlkupera\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_DigitaalinenAlkupera&lt;/a&gt; | 
**matter_annexes** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) | Asian kuvaamiseen tai käsittelyyn olennaisesti kuuluva liitetty asiakirja. | [optional] 
**responsible_party** | [**PlanOperator**](PlanOperator.md) | Vastuutaho | [optional] 
**participation_and_assessment_scheme** | [**ParticipationAndAssessmentScheme**](ParticipationAndAssessmentScheme.md) | Osallistumis- ja arviointisuunnitelma | [optional] 
**source_datas** | [**List[PlanSourceData]**](PlanSourceData.md) | Lähtötietoaineisto | [optional] 
**related_plan_matters** | **List[str]** | Liittyvät kaava asiat (URI) | [optional] 
**plan_matter_phases** | [**List[PlanMatterPhaseUriResponse]**](PlanMatterPhaseUriResponse.md) |  | 
**original_administrative_area_identifiers** | **List[str]** |  | 
**plan_matter_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planmatter/{identifier}) | [optional] [readonly] 

## Example

```python
from ryhti_api_client.models.plan_matter_response import PlanMatterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanMatterResponse from a JSON string
plan_matter_response_instance = PlanMatterResponse.from_json(json)
# print the JSON string representation of the object
print(PlanMatterResponse.to_json())

# convert the object into a dict
plan_matter_response_dict = plan_matter_response_instance.to_dict()
# create an instance of PlanMatterResponse from a dict
plan_matter_response_from_dict = PlanMatterResponse.from_dict(plan_matter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


