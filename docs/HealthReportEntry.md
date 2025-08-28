# HealthReportEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 

## Example

```python
from ryhti_api_client.models.health_report_entry import HealthReportEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HealthReportEntry from a JSON string
health_report_entry_instance = HealthReportEntry.from_json(json)
# print the JSON string representation of the object
print(HealthReportEntry.to_json())

# convert the object into a dict
health_report_entry_dict = health_report_entry_instance.to_dict()
# create an instance of HealthReportEntry from a dict
health_report_entry_from_dict = HealthReportEntry.from_dict(health_report_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


