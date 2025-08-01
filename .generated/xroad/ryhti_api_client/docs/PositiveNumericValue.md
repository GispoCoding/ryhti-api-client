# PositiveNumericValue

Positiivinen numeerinen arvo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Numero | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;positiveNumeric\&quot; | 

## Example

```python
from ryhti_api_client.models.positive_numeric_value import PositiveNumericValue

# TODO update the JSON string below
json = "{}"
# create an instance of PositiveNumericValue from a JSON string
positive_numeric_value_instance = PositiveNumericValue.from_json(json)
# print the JSON string representation of the object
print(PositiveNumericValue.to_json())

# convert the object into a dict
positive_numeric_value_dict = positive_numeric_value_instance.to_dict()
# create an instance of PositiveNumericValue from a dict
positive_numeric_value_from_dict = PositiveNumericValue.from_dict(positive_numeric_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


