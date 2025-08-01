# MotherProperty

Muodostajakiinteistö

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_identifier** | **str** | Kiinteistötunnus | [optional] 
**unseparated_parcel_identifier** | **str** | Määräalatunnus | [optional] 
**contained_area** | [**PositiveNumericValue**](PositiveNumericValue.md) | Positiivinen numeerinen arvo | 
**fully_included** | **bool** | Sisältyy kokonaan | 

## Example

```python
from ryhti_api_client.models.mother_property import MotherProperty

# TODO update the JSON string below
json = "{}"
# create an instance of MotherProperty from a JSON string
mother_property_instance = MotherProperty.from_json(json)
# print the JSON string representation of the object
print(MotherProperty.to_json())

# convert the object into a dict
mother_property_dict = mother_property_instance.to_dict()
# create an instance of MotherProperty from a dict
mother_property_from_dict = MotherProperty.from_dict(mother_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


