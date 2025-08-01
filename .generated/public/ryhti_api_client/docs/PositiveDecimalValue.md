# PositiveDecimalValue

Positiivinen desimaali

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** | Desimaali | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;positiveDecimal\&quot; | 

## Example

```python
from ryhti_api_client.models.positive_decimal_value import PositiveDecimalValue

# TODO update the JSON string below
json = "{}"
# create an instance of PositiveDecimalValue from a JSON string
positive_decimal_value_instance = PositiveDecimalValue.from_json(json)
# print the JSON string representation of the object
print(PositiveDecimalValue.to_json())

# convert the object into a dict
positive_decimal_value_dict = positive_decimal_value_instance.to_dict()
# create an instance of PositiveDecimalValue from a dict
positive_decimal_value_from_dict = PositiveDecimalValue.from_dict(positive_decimal_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


