# CustomValidationProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**errors** | [**List[CustomValidationError]**](CustomValidationError.md) |  | [optional] 
**warnings** | [**List[CustomValidationError]**](CustomValidationError.md) |  | [optional] 

## Example

```python
from ryhti_api_client.models.custom_validation_problem_details import CustomValidationProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValidationProblemDetails from a JSON string
custom_validation_problem_details_instance = CustomValidationProblemDetails.from_json(json)
# print the JSON string representation of the object
print(CustomValidationProblemDetails.to_json())

# convert the object into a dict
custom_validation_problem_details_dict = custom_validation_problem_details_instance.to_dict()
# create an instance of CustomValidationProblemDetails from a dict
custom_validation_problem_details_from_dict = CustomValidationProblemDetails.from_dict(custom_validation_problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


