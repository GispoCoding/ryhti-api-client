# PlanObjectCancellationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_object_cancellation_info_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**cancelled_plan_object_uri** | **str** | Kumottavan kaavakohteen tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planobject/{planObjectKey}) | 
**cancels_entire_plan_object** | **bool** | Kumoaa kohteen kokonaan | 
**validity_geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Osittain kumottaessa kohteen voimaan jäävä geometria | [optional] 

## Example

```python
from ryhti_api_client.models.plan_object_cancellation_info import PlanObjectCancellationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlanObjectCancellationInfo from a JSON string
plan_object_cancellation_info_instance = PlanObjectCancellationInfo.from_json(json)
# print the JSON string representation of the object
print(PlanObjectCancellationInfo.to_json())

# convert the object into a dict
plan_object_cancellation_info_dict = plan_object_cancellation_info_instance.to_dict()
# create an instance of PlanObjectCancellationInfo from a dict
plan_object_cancellation_info_from_dict = PlanObjectCancellationInfo.from_dict(plan_object_cancellation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


