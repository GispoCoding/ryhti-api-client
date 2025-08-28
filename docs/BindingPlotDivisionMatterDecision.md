# BindingPlotDivisionMatterDecision

Sitovan tonttijaon asian päätös

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_plot_division_matter_decision_key** | **str** | Sitovan tonttijaon asian päätösavain | 
**binding_plot_division_matter_decision_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivisionmatterdecision/{guid}) | [optional] [readonly] 
**decision_date** | **date** | Päätöspäivämäärä | 
**date_of_decision** | **date** | Päätöksenantopäivämäärä | 
**date_of_validity** | **date** | Lainvoimaisuuspäivämäärä | 
**decision_documents** | [**List[BindingPlotDivisionAttachmentDocument]**](BindingPlotDivisionAttachmentDocument.md) | Päätösasiakirjat | 
**decision_article** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**decision_text** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | [optional] 
**name** | **str** | Päätöksen nimitys, joka kertoo mitä päätös koskee. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/AlueidenkayttopaatoksenNimi\&quot;&gt;http://uri.suomi.fi/codelist/rytj/AlueidenkayttopaatoksenNimi&lt;/a&gt; | 
**decision_identifier** | **str** | Päätöstunnus | [optional] 
**type_of_decision_maker** | **str** | Päättäjän laji, monijäseninen toimielin tai viranhaltija. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija\&quot;&gt;http://uri.suomi.fi/codelist/rytj/PaatoksenTekija&lt;/a&gt; | 
**statute** | [**Statute**](Statute.md) | Ohjaava säädös | [optional] 
**decision_maker** | [**BindingPlotDivisionOperator**](BindingPlotDivisionOperator.md) | Päätöksentekijä | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division_matter_decision import BindingPlotDivisionMatterDecision

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivisionMatterDecision from a JSON string
binding_plot_division_matter_decision_instance = BindingPlotDivisionMatterDecision.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivisionMatterDecision.to_json())

# convert the object into a dict
binding_plot_division_matter_decision_dict = binding_plot_division_matter_decision_instance.to_dict()
# create an instance of BindingPlotDivisionMatterDecision from a dict
binding_plot_division_matter_decision_from_dict = BindingPlotDivisionMatterDecision.from_dict(binding_plot_division_matter_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


