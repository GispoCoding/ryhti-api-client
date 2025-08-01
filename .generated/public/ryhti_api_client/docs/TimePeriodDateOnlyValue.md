# TimePeriodDateOnlyValue

TimePeriodDateOnly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **date** | Alkupäivä | [optional] 
**end** | **date** | Loppupäivä | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;timePeriodDateOnly\&quot; | 

## Example

```python
from ryhti_api_client.models.time_period_date_only_value import TimePeriodDateOnlyValue

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodDateOnlyValue from a JSON string
time_period_date_only_value_instance = TimePeriodDateOnlyValue.from_json(json)
# print the JSON string representation of the object
print(TimePeriodDateOnlyValue.to_json())

# convert the object into a dict
time_period_date_only_value_dict = time_period_date_only_value_instance.to_dict()
# create an instance of TimePeriodDateOnlyValue from a dict
time_period_date_only_value_from_dict = TimePeriodDateOnlyValue.from_dict(time_period_date_only_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


