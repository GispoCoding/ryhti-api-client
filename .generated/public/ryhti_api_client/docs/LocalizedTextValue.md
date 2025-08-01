# LocalizedTextValue

Lokalisoitu teksti

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | [**LanguageString**](LanguageString.md) | Kielistetty teksti | [optional] 
**syntax** | **str** | Syntaksi | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;localizedText\&quot; | 

## Example

```python
from ryhti_api_client.models.localized_text_value import LocalizedTextValue

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedTextValue from a JSON string
localized_text_value_instance = LocalizedTextValue.from_json(json)
# print the JSON string representation of the object
print(LocalizedTextValue.to_json())

# convert the object into a dict
localized_text_value_dict = localized_text_value_instance.to_dict()
# create an instance of LocalizedTextValue from a dict
localized_text_value_from_dict = LocalizedTextValue.from_dict(localized_text_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


