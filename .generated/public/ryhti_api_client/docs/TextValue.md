# TextValue

Teksti

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Teksti | [optional] 
**syntax** | **str** | Syntaksi | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;text\&quot; | 

## Example

```python
from ryhti_api_client.models.text_value import TextValue

# TODO update the JSON string below
json = "{}"
# create an instance of TextValue from a JSON string
text_value_instance = TextValue.from_json(json)
# print the JSON string representation of the object
print(TextValue.to_json())

# convert the object into a dict
text_value_dict = text_value_instance.to_dict()
# create an instance of TextValue from a dict
text_value_from_dict = TextValue.from_dict(text_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


