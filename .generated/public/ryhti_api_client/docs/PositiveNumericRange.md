# PositiveNumericRange

Positiivinen arvoväli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_value** | **int** | Minimiarvo | [optional] 
**maximum_value** | **int** | Maksimiarvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;positiveNumericRange\&quot; | 

## Example

```python
from ryhti_api_client.models.positive_numeric_range import PositiveNumericRange

# TODO update the JSON string below
json = "{}"
# create an instance of PositiveNumericRange from a JSON string
positive_numeric_range_instance = PositiveNumericRange.from_json(json)
# print the JSON string representation of the object
print(PositiveNumericRange.to_json())

# convert the object into a dict
positive_numeric_range_dict = positive_numeric_range_instance.to_dict()
# create an instance of PositiveNumericRange from a dict
positive_numeric_range_from_dict = PositiveNumericRange.from_dict(positive_numeric_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


