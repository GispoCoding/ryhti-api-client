# BindingPlotDivisionMatterPhase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_cycle_status** | **str** | Tonttijakosuunnitelman elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/sitovanTonttijaonElinkaarenTila\&quot;&gt;http://uri.suomi.fi/codelist/rytj/sitovanTonttijaonElinkaarenTila&lt;/a&gt; | 
**binding_plot_division_matter_phase_key** | **str** | Sitovan tonttijaon asian vaihe avain | 
**binding_plot_division_matter_phase_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivisionmatterphase/{guid}) | [optional] [readonly] 
**decision** | [**BindingPlotDivisionMatterDecision**](BindingPlotDivisionMatterDecision.md) | Päätös | [optional] 
**approved_plan_decision_uri** | **str** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/plandecision/{plandecisionkey}) hyväksytyn kaavan päätökseen. | [optional] 
**binding_plot_division** | [**BindingPlotDivision**](BindingPlotDivision.md) | Sitova tonttijako | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division_matter_phase import BindingPlotDivisionMatterPhase

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivisionMatterPhase from a JSON string
binding_plot_division_matter_phase_instance = BindingPlotDivisionMatterPhase.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivisionMatterPhase.to_json())

# convert the object into a dict
binding_plot_division_matter_phase_dict = binding_plot_division_matter_phase_instance.to_dict()
# create an instance of BindingPlotDivisionMatterPhase from a dict
binding_plot_division_matter_phase_from_dict = BindingPlotDivisionMatterPhase.from_dict(binding_plot_division_matter_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


