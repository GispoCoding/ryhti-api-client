# NumericRange

Numeerinen arvoväli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_value** | **int** | Minimiarvo | [optional] 
**maximum_value** | **int** | Maksimiarvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;numericRange\&quot; | 

## Example

```python
from ryhti_api_client.models.numeric_range import NumericRange

# TODO update the JSON string below
json = "{}"
# create an instance of NumericRange from a JSON string
numeric_range_instance = NumericRange.from_json(json)
# print the JSON string representation of the object
print(NumericRange.to_json())

# convert the object into a dict
numeric_range_dict = numeric_range_instance.to_dict()
# create an instance of NumericRange from a dict
numeric_range_from_dict = NumericRange.from_dict(numeric_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


