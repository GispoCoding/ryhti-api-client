# Statute

Säädösviite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_of_statute** | [**LanguageString**](LanguageString.md) | Lokalisoitu merkkijono-luokka eri kielille. Lisää vähintään yksi kieli. | 
**number_of_statute_collection** | **int** |  | 
**year_of_statute_collection** | **int** |  | 
**chapter** | **int** | Luku | [optional] 
**section** | **int** | Pykälä | [optional] 
**subsections** | **List[int]** | Momentit | [optional] 
**paragraphs** | **List[int]** | Kohdat | [optional] 
**subparagraphs** | **List[str]** | Alakohdat | [optional] 

## Example

```python
from ryhti_api_client.models.statute import Statute

# TODO update the JSON string below
json = "{}"
# create an instance of Statute from a JSON string
statute_instance = Statute.from_json(json)
# print the JSON string representation of the object
print(Statute.to_json())

# convert the object into a dict
statute_dict = statute_instance.to_dict()
# create an instance of Statute from a dict
statute_from_dict = Statute.from_dict(statute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


