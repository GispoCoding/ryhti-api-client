# TimePeriodValue

TimePeriod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_utc** | **datetime** | Alkuaika | [optional] 
**end_utc** | **datetime** | Loppuaika | [optional] 
**data_type** | **str** | Pakollinen arvo: \&quot;timePeriod\&quot; | 

## Example

```python
from ryhti_api_client.models.time_period_value import TimePeriodValue

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodValue from a JSON string
time_period_value_instance = TimePeriodValue.from_json(json)
# print the JSON string representation of the object
print(TimePeriodValue.to_json())

# convert the object into a dict
time_period_value_dict = time_period_value_instance.to_dict()
# create an instance of TimePeriodValue from a dict
time_period_value_from_dict = TimePeriodValue.from_dict(time_period_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


