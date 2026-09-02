# PlanEffectsPlot

Liittyvä tonttijakotontti  KaavanVaikutukset Tonttijakotonttikohtaisesti

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_in_accordance_with_plan** | **bool** | Onko kaavan mukainen | 
**area_reservation_type_uris** | **List[str]** | Aluevaraus: kaavanmääräyslaji.  Lista kaavanmääräyslajin URI-tunnisteita koodistosta http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayslaji | [optional] 
**area_reservation_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey}) kaavassa osoitettuun aluevarauksen kaavamääräykseen. | [optional] 
**volume_of_building_regulation_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planregulationkey})  kaavassa osoitettuun rakentamisen määrän kaavamääräykseen. | [optional] 
**area_reservation_letter_identifier** | **str** | Aluevarauksen kirjaintunnus | [optional] 
**permitted_building_area** | **int** | Rakentamisen määrä, kerrosala m2 | [optional] 
**permitted_building_volume** | **int** | Rakentamisen määrä, rakennustilavuus m3 | [optional] 
**plot_division_plot_key** | **UUID** | Tonttijakotontin tunniste (PlotDivisionPlotKey), johon kaavan vaikutus kohdistuu.  Pakollinen | [optional] 

## Example

```python
from ryhti_api_client.models.plan_effects_plot import PlanEffectsPlot

# TODO update the JSON string below
json = "{}"
# create an instance of PlanEffectsPlot from a JSON string
plan_effects_plot_instance = PlanEffectsPlot.from_json(json)
# print the JSON string representation of the object
print(PlanEffectsPlot.to_json())

# convert the object into a dict
plan_effects_plot_dict = plan_effects_plot_instance.to_dict()
# create an instance of PlanEffectsPlot from a dict
plan_effects_plot_from_dict = PlanEffectsPlot.from_dict(plan_effects_plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


