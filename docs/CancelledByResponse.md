# CancelledByResponse

Kuvaa kumoamistiedon, eli minkä kaavan toimesta tämä kaava-asia on kumottu.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_cancellation_key** | **UUID** | Kumoamistiedon avain | [optional] 
**permanent_plan_identifier** | **str** | Kumoavan kaavan pysyvä kaavatunnus | [optional] 
**date_of_validity** | **date** | Voimaantulopäivämäärä | [optional] 

## Example

```python
from ryhti_api_client.models.cancelled_by_response import CancelledByResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledByResponse from a JSON string
cancelled_by_response_instance = CancelledByResponse.from_json(json)
# print the JSON string representation of the object
print(CancelledByResponse.to_json())

# convert the object into a dict
cancelled_by_response_dict = cancelled_by_response_instance.to_dict()
# create an instance of CancelledByResponse from a dict
cancelled_by_response_from_dict = CancelledByResponse.from_dict(cancelled_by_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


