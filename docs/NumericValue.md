# NumericValue

Numeerinen arvo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Numero | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;numeric\&quot; | 

## Example

```python
from ryhti_api_client.models.numeric_value import NumericValue

# TODO update the JSON string below
json = "{}"
# create an instance of NumericValue from a JSON string
numeric_value_instance = NumericValue.from_json(json)
# print the JSON string representation of the object
print(NumericValue.to_json())

# convert the object into a dict
numeric_value_dict = numeric_value_instance.to_dict()
# create an instance of NumericValue from a dict
numeric_value_from_dict = NumericValue.from_dict(numeric_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


