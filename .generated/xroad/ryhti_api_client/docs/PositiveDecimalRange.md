# PositiveDecimalRange

Positiivinen desimaaliarvoväli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_value** | **float** | Minimiarvo | [optional] 
**maximum_value** | **float** | Maksimiarvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;positiveDecimalRange\&quot; | 

## Example

```python
from ryhti_api_client.models.positive_decimal_range import PositiveDecimalRange

# TODO update the JSON string below
json = "{}"
# create an instance of PositiveDecimalRange from a JSON string
positive_decimal_range_instance = PositiveDecimalRange.from_json(json)
# print the JSON string representation of the object
print(PositiveDecimalRange.to_json())

# convert the object into a dict
positive_decimal_range_dict = positive_decimal_range_instance.to_dict()
# create an instance of PositiveDecimalRange from a dict
positive_decimal_range_from_dict = PositiveDecimalRange.from_dict(positive_decimal_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


