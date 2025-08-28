# BindingPlotDivisionMatterCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**description** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**binding_plot_division_type** | **str** | Sitovan tonttijaon laji. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/sitovanTonttijaonLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/sitovanTonttijaonLaji&lt;/a&gt; | 
**permanent_binding_plot_division_identifier** | **str** | sitovan tonttijaon pysyvä tunnus | 
**producer_binding_plot_division_identifier** | **str** | kunnan antama sitovan tonttijaon tunnus | [optional] 
**case_identifiers** | **List[str]** | asianhallintatunnukset | [optional] 
**record_numbers** | **List[str]** | diaarinumerot | [optional] 
**time_of_initiation** | **date** | vireilletulopäivämäärä | 
**administrative_area_identifiers** | **List[str]** | hallinnollisen alueen tunnukset | 
**responsible_party** | [**BindingPlotDivisionOperator**](BindingPlotDivisionOperator.md) | Vastuutaho | [optional] 
**related_binding_plot_division_matters** | **List[str]** | Liittyvät asiat | [optional] 
**matter_annexes** | [**List[BindingPlotDivisionAttachmentDocument]**](BindingPlotDivisionAttachmentDocument.md) | AsianLiitteet | [optional] 
**phases** | [**List[BindingPlotDivisionMatterPhase]**](BindingPlotDivisionMatterPhase.md) | Vaiheet | 
**original_administrative_area_identifiers** | **List[str]** |  | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division_matter_create import BindingPlotDivisionMatterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivisionMatterCreate from a JSON string
binding_plot_division_matter_create_instance = BindingPlotDivisionMatterCreate.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivisionMatterCreate.to_json())

# convert the object into a dict
binding_plot_division_matter_create_dict = binding_plot_division_matter_create_instance.to_dict()
# create an instance of BindingPlotDivisionMatterCreate from a dict
binding_plot_division_matter_create_from_dict = BindingPlotDivisionMatterCreate.from_dict(binding_plot_division_matter_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


