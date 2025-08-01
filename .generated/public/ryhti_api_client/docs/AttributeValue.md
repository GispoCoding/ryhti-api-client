# AttributeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Enumeraatio joka määrittää Arvo-luokkien (Domain.ValueObjects.AttributeValue) tyypin.  Jokaisella konkreettisella Arvo-luokan (Domain.ValueObjects.AttributeValue) toteutuksella tulee olla sitä vastaava DataType enumeraation arvo. | [optional] 

## Example

```python
from ryhti_api_client.models.attribute_value import AttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeValue from a JSON string
attribute_value_instance = AttributeValue.from_json(json)
# print the JSON string representation of the object
print(AttributeValue.to_json())

# convert the object into a dict
attribute_value_dict = attribute_value_instance.to_dict()
# create an instance of AttributeValue from a dict
attribute_value_from_dict = AttributeValue.from_dict(attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


