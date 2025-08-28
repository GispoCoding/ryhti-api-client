# LanguageString

Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fin** | **str** | suomi | [optional] 
**swe** | **str** | ruotsi | [optional] 
**smn** | **str** | inarinsaame | [optional] 
**sms** | **str** | koltansaame | [optional] 
**sme** | **str** | pohjoissaame | [optional] 
**eng** | **str** | englanti | [optional] 

## Example

```python
from ryhti_api_client.models.language_string import LanguageString

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageString from a JSON string
language_string_instance = LanguageString.from_json(json)
# print the JSON string representation of the object
print(LanguageString.to_json())

# convert the object into a dict
language_string_dict = language_string_instance.to_dict()
# create an instance of LanguageString from a dict
language_string_from_dict = LanguageString.from_dict(language_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


