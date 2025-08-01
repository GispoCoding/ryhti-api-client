# CodeValue

Koodiston arvo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Koodiston arvo (uri) | [optional] 
**code_list** | **str** | Koodisto | [optional] 
**title** | [**LanguageString**](LanguageString.md) | Nimi | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;code\&quot; | 

## Example

```python
from ryhti_api_client.models.code_value import CodeValue

# TODO update the JSON string below
json = "{}"
# create an instance of CodeValue from a JSON string
code_value_instance = CodeValue.from_json(json)
# print the JSON string representation of the object
print(CodeValue.to_json())

# convert the object into a dict
code_value_dict = code_value_instance.to_dict()
# create an instance of CodeValue from a dict
code_value_from_dict = CodeValue.from_dict(code_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


