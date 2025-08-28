# HealthReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [readonly] 
**total_duration** | **str** |  | [optional] [readonly] 
**entries** | [**Dict[str, HealthReportEntry]**](HealthReportEntry.md) |  | [optional] [readonly] 

## Example

```python
from ryhti_api_client.models.health_report import HealthReport

# TODO update the JSON string below
json = "{}"
# create an instance of HealthReport from a JSON string
health_report_instance = HealthReport.from_json(json)
# print the JSON string representation of the object
print(HealthReport.to_json())

# convert the object into a dict
health_report_dict = health_report_instance.to_dict()
# create an instance of HealthReport from a dict
health_report_from_dict = HealthReport.from_dict(health_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


