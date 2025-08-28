# LandUseRestrictionOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**land_use_restriction_operator_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus. | 
**land_use_restriction_operator_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/landuserestrictionoperator/{guid}) | [optional] [readonly] 
**first_name** | **str** | Toimijan etunimi | [optional] 
**last_name** | **str** | Toimijan sukunimi | [optional] 
**title** | **str** | Toimijan nimike | [optional] 
**organization_name** | **str** | Toimijan organisaation nimi. | [optional] 
**business_id** | **str** | Toimijan organisaation y-tunnus. | [optional] 

## Example

```python
from ryhti_api_client.models.land_use_restriction_operator import LandUseRestrictionOperator

# TODO update the JSON string below
json = "{}"
# create an instance of LandUseRestrictionOperator from a JSON string
land_use_restriction_operator_instance = LandUseRestrictionOperator.from_json(json)
# print the JSON string representation of the object
print(LandUseRestrictionOperator.to_json())

# convert the object into a dict
land_use_restriction_operator_dict = land_use_restriction_operator_instance.to_dict()
# create an instance of LandUseRestrictionOperator from a dict
land_use_restriction_operator_from_dict = LandUseRestrictionOperator.from_dict(land_use_restriction_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


