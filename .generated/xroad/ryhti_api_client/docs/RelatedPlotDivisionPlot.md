# RelatedPlotDivisionPlot

LiittyväTonttijakotontti

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_uri** | **str** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/plotdivisionplot/{plotdivisionplotkey}) sitovassa tonttijaossa osoitettuun tonttijakotonttiin. | 
**related_plans** | [**List[RelatedPlan]**](RelatedPlan.md) | Tonttijakotontin alueelle kohdistuvan vaikuttavan kaavan pysyvä kaavatunnus | 
**area_reservation_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey}) kaavassa osoitettuun aluevarauksen kaavamääräykseen. | [optional] 
**volume_of_building_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey}) kaavassa osoitettuun rakentamisen määrän kaavamääräykseen. | [optional] 

## Example

```python
from ryhti_api_client.models.related_plot_division_plot import RelatedPlotDivisionPlot

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedPlotDivisionPlot from a JSON string
related_plot_division_plot_instance = RelatedPlotDivisionPlot.from_json(json)
# print the JSON string representation of the object
print(RelatedPlotDivisionPlot.to_json())

# convert the object into a dict
related_plot_division_plot_dict = related_plot_division_plot_instance.to_dict()
# create an instance of RelatedPlotDivisionPlot from a dict
related_plot_division_plot_from_dict = RelatedPlotDivisionPlot.from_dict(related_plot_division_plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


