# TimePeriodDateOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **date** |  | [optional] 
**end** | **date** |  | [optional] 

## Example

```python
from ryhti_api_client.models.time_period_date_only import TimePeriodDateOnly

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodDateOnly from a JSON string
time_period_date_only_instance = TimePeriodDateOnly.from_json(json)
# print the JSON string representation of the object
print(TimePeriodDateOnly.to_json())

# convert the object into a dict
time_period_date_only_dict = time_period_date_only_instance.to_dict()
# create an instance of TimePeriodDateOnly from a dict
time_period_date_only_from_dict = TimePeriodDateOnly.from_dict(time_period_date_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


