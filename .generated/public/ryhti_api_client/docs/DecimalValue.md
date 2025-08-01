# DecimalValue

Desimaaliluku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** | Desimaaliluku | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;decimal\&quot; | 

## Example

```python
from ryhti_api_client.models.decimal_value import DecimalValue

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalValue from a JSON string
decimal_value_instance = DecimalValue.from_json(json)
# print the JSON string representation of the object
print(DecimalValue.to_json())

# convert the object into a dict
decimal_value_dict = decimal_value_instance.to_dict()
# create an instance of DecimalValue from a dict
decimal_value_from_dict = DecimalValue.from_dict(decimal_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


