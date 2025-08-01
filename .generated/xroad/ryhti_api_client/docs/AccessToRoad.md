# AccessToRoad

Kulkuyhteys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_to_road_key** | **str** | Kulkuyhteyden avain | 
**access_to_road_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/accesstoroad/{guid}) | [optional] [readonly] 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Aluegeometria (Geometriatyypin oltava Polygon tai MultiPolygon) | 
**plot_division_plot_keys** | **List[str]** | Tonttijakotontit joille kulkuyhteys | 

## Example

```python
from ryhti_api_client.models.access_to_road import AccessToRoad

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToRoad from a JSON string
access_to_road_instance = AccessToRoad.from_json(json)
# print the JSON string representation of the object
print(AccessToRoad.to_json())

# convert the object into a dict
access_to_road_dict = access_to_road_instance.to_dict()
# create an instance of AccessToRoad from a dict
access_to_road_from_dict = AccessToRoad.from_dict(access_to_road_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


