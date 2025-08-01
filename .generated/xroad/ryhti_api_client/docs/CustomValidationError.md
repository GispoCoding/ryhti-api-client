# CustomValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**class_key** | **str** |  | [optional] 

## Example

```python
from ryhti_api_client.models.custom_validation_error import CustomValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValidationError from a JSON string
custom_validation_error_instance = CustomValidationError.from_json(json)
# print the JSON string representation of the object
print(CustomValidationError.to_json())

# convert the object into a dict
custom_validation_error_dict = custom_validation_error_instance.to_dict()
# create an instance of CustomValidationError from a dict
custom_validation_error_from_dict = CustomValidationError.from_dict(custom_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


