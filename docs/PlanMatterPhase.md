# PlanMatterPhase

Kaava-asian vaihe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_matter_phase_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**life_cycle_status** | **str** | Asian elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari&lt;/a&gt; | 
**geographical_area** | [**RyhtiGeometry**](RyhtiGeometry.md) | Aluerajaus | 
**handling_event** | [**HandlingEvent**](HandlingEvent.md) | Käsittelytapahtuma | [optional] 
**interaction_events** | [**List[InteractionEvent]**](InteractionEvent.md) | Vuorovaikutustapahtuma | [optional] 
**plan_decision** | [**PlanDecision**](PlanDecision.md) | Kaavapäätös | [optional] 

## Example

```python
from ryhti_api_client.models.plan_matter_phase import PlanMatterPhase

# TODO update the JSON string below
json = "{}"
# create an instance of PlanMatterPhase from a JSON string
plan_matter_phase_instance = PlanMatterPhase.from_json(json)
# print the JSON string representation of the object
print(PlanMatterPhase.to_json())

# convert the object into a dict
plan_matter_phase_dict = plan_matter_phase_instance.to_dict()
# create an instance of PlanMatterPhase from a dict
plan_matter_phase_from_dict = PlanMatterPhase.from_dict(plan_matter_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


