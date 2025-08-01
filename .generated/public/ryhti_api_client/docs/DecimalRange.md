# DecimalRange

Desimaaliarvoväli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_value** | **float** | Minimiarvo | [optional] 
**maximum_value** | **float** | Maksimiarvo | [optional] 
**unit_of_measure** | **str** | Mittayksikkö | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;decimalRange\&quot; | 

## Example

```python
from ryhti_api_client.models.decimal_range import DecimalRange

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalRange from a JSON string
decimal_range_instance = DecimalRange.from_json(json)
# print the JSON string representation of the object
print(DecimalRange.to_json())

# convert the object into a dict
decimal_range_dict = decimal_range_instance.to_dict()
# create an instance of DecimalRange from a dict
decimal_range_from_dict = DecimalRange.from_dict(decimal_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


