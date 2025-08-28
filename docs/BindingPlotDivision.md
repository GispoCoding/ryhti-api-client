# BindingPlotDivision

Sitova tonttijako

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_plot_division_key** | **str** | Sitova tonttijako avain | 
**binding_plot_division_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivision/{guid}) | [optional] [readonly] 
**binding_plot_division_cancellation_infos** | [**List[BindingPlotDivisionCancellationInfo]**](BindingPlotDivisionCancellationInfo.md) | Sitovan tonttijaon kumoutumistieto | [optional] 
**plot_division_plots** | [**List[PlotDivisionPlot]**](PlotDivisionPlot.md) | Tonttijakotontit | 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | Voimassaolo aika | 
**geographical_area** | [**RyhtiGeometry**](RyhtiGeometry.md) | Aluerajaus | 
**boundary_points** | [**List[BoundaryPoint]**](BoundaryPoint.md) | Rajapisteet | 
**accesses_to_road** | [**List[AccessToRoad]**](AccessToRoad.md) | Kulkuhteydet | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division import BindingPlotDivision

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivision from a JSON string
binding_plot_division_instance = BindingPlotDivision.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivision.to_json())

# convert the object into a dict
binding_plot_division_dict = binding_plot_division_instance.to_dict()
# create an instance of BindingPlotDivision from a dict
binding_plot_division_from_dict = BindingPlotDivision.from_dict(binding_plot_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


