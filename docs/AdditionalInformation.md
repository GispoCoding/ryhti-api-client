# AdditionalInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Määräystä täydentävä tieto, jolla ohjataan alueidenkäyttöä ja rakentamista. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayksen_Lisatiedonlaji\&quot;&gt;http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayksen_Lisatiedonlaji&lt;/a&gt; | 
**value** | [**AdditionalInformationValue**](AdditionalInformationValue.md) |  | [optional] 

## Example

```python
from ryhti_api_client.models.additional_information import AdditionalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInformation from a JSON string
additional_information_instance = AdditionalInformation.from_json(json)
# print the JSON string representation of the object
print(AdditionalInformation.to_json())

# convert the object into a dict
additional_information_dict = additional_information_instance.to_dict()
# create an instance of AdditionalInformation from a dict
additional_information_from_dict = AdditionalInformation.from_dict(additional_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


