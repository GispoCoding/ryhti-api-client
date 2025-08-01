# PlanCancellationInfo

Kaavan kumoamistieto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_cancellation_info_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_cancellation_info_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plancancellationinfo/{guid}) | [optional] [readonly] 
**cancelled_plan_uri** | **str** | Kumottavan hyväkstytyn kaavan tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/plan/{planKey}) | 
**cancels_entire_plan** | **bool** | Kumoaa kaavan kokonaan | 
**cancelled_plan_object_uris** | **List[str]** | Kumottavan kaavakohteen tunnukset URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planobject/{planObjectKey}) | [optional] 
**cancelled_regulation_uris** | **List[str]** | Kumottavan määräyksen tunnukset URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planregulation/{planRegulationKey}) | [optional] 
**cancelled_recommendation_uris** | **List[str]** | Kumottavan suosituksen tunnukset URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planrecommendation/{planRecommendationKey}) | [optional] 
**cancelled_group_relations** | [**List[CancelledGroupRelations]**](CancelledGroupRelations.md) | Kumottavan ryhmän kohdistus. Kuvaa kaavakohteesta kumoutuvat kaavamääräysryhmät. | [optional] 

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


