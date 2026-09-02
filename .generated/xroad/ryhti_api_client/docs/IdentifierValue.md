# IdentifierValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Pakollinen arvo: \&quot;Identifier\&quot; | 
**identifier** | **str** | Tunnus | [optional] 
**register_identifier** | **str** | Järjestelmän tunnus | [optional] 
**register_name** | [**LanguageString**](LanguageString.md) | Järjestelmän nimi | [optional] 

## Example

```python
from ryhti_api_client.models.identifier_value import IdentifierValue

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierValue from a JSON string
identifier_value_instance = IdentifierValue.from_json(json)
# print the JSON string representation of the object
print(IdentifierValue.to_json())

# convert the object into a dict
identifier_value_dict = identifier_value_instance.to_dict()
# create an instance of IdentifierValue from a dict
identifier_value_from_dict = IdentifierValue.from_dict(identifier_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


