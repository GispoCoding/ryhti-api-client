# PlanEffects

KaavanVaikutukset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Kaavan vaikutuksen laji. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavanVaikutuksenLaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavanVaikutuksenLaji&lt;/a&gt; | 
**binding_plot_division_uri** | **str** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivision/{bindingplotdivisionkey}) sitovaan tonttijakoon. | 
**fully_included** | **bool** | Jos arvo on true, kaavan vaikutus kohdistuu sitovaan tonttijakoon kokonaisuudessaan, muuten tonttijakotontti kohtaisesti. | [optional] 
**related_plot_division_plots** | [**List[RelatedPlotDivisionPlot]**](RelatedPlotDivisionPlot.md) | Tonttijakotontin yksilöivätunnus, jota vaikutus koskee. | 

## Example

```python
from ryhti_api_client.models.plan_effects import PlanEffects

# TODO update the JSON string below
json = "{}"
# create an instance of PlanEffects from a JSON string
plan_effects_instance = PlanEffects.from_json(json)
# print the JSON string representation of the object
print(PlanEffects.to_json())

# convert the object into a dict
plan_effects_dict = plan_effects_instance.to_dict()
# create an instance of PlanEffects from a dict
plan_effects_from_dict = PlanEffects.from_dict(plan_effects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


