# PartiallyCancelledPlanObjectInfo

OsittainKumottavanKaavakohteenTieto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_plan_uri** | **str** | Kumottavan hyväkstytyn kaavan tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/plan/{planKey}) | 
**partially_cancelled_plan_object_uri** | **str** | Kumottavan kaavakohteen tunnus uri-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planobject/{planObjectKey}) | 
**validity_geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Osittain kumottavan kaavakohteen voimaan jäävän alueen geometria. | 

## Example

```python
from ryhti_api_client.models.partially_cancelled_plan_object_info import PartiallyCancelledPlanObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PartiallyCancelledPlanObjectInfo from a JSON string
partially_cancelled_plan_object_info_instance = PartiallyCancelledPlanObjectInfo.from_json(json)
# print the JSON string representation of the object
print(PartiallyCancelledPlanObjectInfo.to_json())

# convert the object into a dict
partially_cancelled_plan_object_info_dict = partially_cancelled_plan_object_info_instance.to_dict()
# create an instance of PartiallyCancelledPlanObjectInfo from a dict
partially_cancelled_plan_object_info_from_dict = PartiallyCancelledPlanObjectInfo.from_dict(partially_cancelled_plan_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


