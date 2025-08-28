# LandUseRestriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**land_use_restriction_key** | **str** | Avain | 
**land_use_restriction_uri** | **str** |  | [optional] [readonly] 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | Voimassaoloaika | 
**land_use_restriction_objects** | [**List[LandUseRestrictionObject]**](LandUseRestrictionObject.md) | Alueidenkäytön rajoituskohde | 

## Example

```python
from ryhti_api_client.models.land_use_restriction import LandUseRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestriction from a JSON string
land_use_restriction_instance = LandUseRestriction.from_json(json)
# print the JSON string representation of the object
print(LandUseRestriction.to_json())

# convert the object into a dict
land_use_restriction_dict = land_use_restriction_instance.to_dict()
# create an instance of LandUseRestriction from a dict
land_use_restriction_from_dict = LandUseRestriction.from_dict(land_use_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


