# PlanReport

Kaavaselostus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_report_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_report_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/planreport/{guid}) | [optional] [readonly] 
**attachment_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) |  | 

## Example

```python
from ryhti_api_client.models.plan_report import PlanReport

# TODO update the JSON string below
json = "{}"
# create an instance of PlanReport from a JSON string
plan_report_instance = PlanReport.from_json(json)
# print the JSON string representation of the object
print(PlanReport.to_json())

# convert the object into a dict
plan_report_dict = plan_report_instance.to_dict()
# create an instance of PlanReport from a dict
plan_report_from_dict = PlanReport.from_dict(plan_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


