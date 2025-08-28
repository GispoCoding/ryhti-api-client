# PlanCancellationInfo

Kumoamistieto. Kuvaa kaavan kumoamista. Kumoamistieto voi kumota kaavan kokonaan tai osittain.  On joko Plan- tai PlanDecision-luokan lapsi.                Jos kumotaan kaavalla niin:  1) Kaava kumotaan kokonaan.  Tällöin ei saa olla kumoamistietoja kaavakohteista, määräyksistä tai suosituksista.  Kumoaa aina koko kaavan. Jos se on Plan-luokalla niin kumotaan se plan, millä sijaitsee.  Jos se on PlanDecision-luokalla niin kumotaan se plan, mihin päätös liittyy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_cancellation_info_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_cancellation_info_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plancancellationinfo/{guid}) | [optional] [readonly] 
**cancelled_plan_uri** | **str** | Kumottavan hyväkstytyn kaavan tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/plan/{planKey}) | 
**cancels_entire_plan** | **bool** | Kumoaa kaavan kokonaan | 
**cancelled_group_relations** | [**List[CancelledGroupRelations]**](CancelledGroupRelations.md) | Kumottavan ryhmän kohdistus. Kuvaa kaavakohteesta kumoutuvat kaavamääräysryhmät. | [optional] 
**plan_object_cancellation_infos** | [**List[PlanObjectCancellationInfo]**](PlanObjectCancellationInfo.md) | Kumottavat kaavakohteet | [optional] 

## Example

```python
from ryhti_api_client.models.plan_cancellation_info import PlanCancellationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlanCancellationInfo from a JSON string
plan_cancellation_info_instance = PlanCancellationInfo.from_json(json)
# print the JSON string representation of the object
print(PlanCancellationInfo.to_json())

# convert the object into a dict
plan_cancellation_info_dict = plan_cancellation_info_instance.to_dict()
# create an instance of PlanCancellationInfo from a dict
plan_cancellation_info_from_dict = PlanCancellationInfo.from_dict(plan_cancellation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


