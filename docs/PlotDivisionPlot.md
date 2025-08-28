# PlotDivisionPlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plot_division_plot_key** | **str** | Tonttijakotontin avain | 
**plot_division_plot_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plotdivisionplot/{guid}) | [optional] [readonly] 
**plot_division_plot_identifier** | **str** | Tonttijakotontin tunnus | 
**area** | [**PositiveNumericValue**](PositiveNumericValue.md) | Positiivinen numeerinen arvo | [optional] 
**projected_area** | [**PositiveNumericValue**](PositiveNumericValue.md) | Positiivinen numeerinen arvo | [optional] 
**area_reservations** | **List[str]** | Aluvaraukset | 
**area_reservation_letter_identifier** | **str** | Aluevarauksen kirjaintunnus | 
**volume_of_building** | [**PositiveNumericValue**](PositiveNumericValue.md) | Positiivinen numeerinen arvo | 
**mother_properties** | [**List[MotherProperty]**](MotherProperty.md) | Muodostajakiinteistöt | 
**relation_to_basic_property** | **str** | Suhde peruskiinteistöön. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_SuhdePeruskiinteistoon\&quot; /&gt; | [optional] 
**related_plans** | [**List[RelatedPlan]**](RelatedPlan.md) | Liittyvät kaavat | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Geometria | 
**vertical_limit** | [**DecimalRange**](DecimalRange.md) | Desimaaliarvoväli | [optional] 
**area_reservation_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey}) kaavassa osoitettuun aluevarauksen kaavamääräykseen. | [optional] 
**volume_of_building_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey}) kaavassa osoitettuun rakentamisen määrän kaavamääräykseen. | [optional] 

## Example

```python
from ryhti_api_client.models.plot_division_plot import PlotDivisionPlot

# TODO update the JSON string below
json = "{}"
# create an instance of PlotDivisionPlot from a JSON string
plot_division_plot_instance = PlotDivisionPlot.from_json(json)
# print the JSON string representation of the object
print(PlotDivisionPlot.to_json())

# convert the object into a dict
plot_division_plot_dict = plot_division_plot_instance.to_dict()
# create an instance of PlotDivisionPlot from a dict
plot_division_plot_from_dict = PlotDivisionPlot.from_dict(plot_division_plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


