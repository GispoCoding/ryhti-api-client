# LandUseRestrictionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**land_use_restriction_object_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus. | 
**land_use_restriction_object_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/landuserestrictionobject/{guid}) | [optional] [readonly] 
**related_properties** | **List[str]** | Tieto liittyvistä kiinteistöistä, joita rajoitus koskee | [optional] 
**related_plans** | [**List[RelatedPlan]**](RelatedPlan.md) | Alueidenkäytön rajoituskohteen alueelle kohdistuvan kaavan pysyvä kaavatunnus | [optional] 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Geometria-attribuutin arvon tulee olla alue, 3-ulotteinen kappale, monialue tai monikappale. | 

## Example

```python
from ryhti_api_client.models.land_use_restriction_object import LandUseRestrictionObject

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionObject from a JSON string
land_use_restriction_object_instance = LandUseRestrictionObject.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionObject.to_json())

# convert the object into a dict
land_use_restriction_object_dict = land_use_restriction_object_instance.to_dict()
# create an instance of LandUseRestrictionObject from a dict
land_use_restriction_object_from_dict = LandUseRestrictionObject.from_dict(land_use_restriction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


