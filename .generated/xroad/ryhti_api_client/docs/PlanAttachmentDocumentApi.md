# ryhti_api_client.PlanAttachmentDocumentApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_plan_attachment_document_attachment_document_key_file_get**](PlanAttachmentDocumentApi.md#api_plan_attachment_document_attachment_document_key_file_get) | **GET** /api/PlanAttachmentDocument/{attachmentDocumentKey}/file | Liiteasiakirjan tiedoston hakeminen liiteasiakirjan avaimella.


# **api_plan_attachment_document_attachment_document_key_file_get**
> object api_plan_attachment_document_attachment_document_key_file_get(attachment_document_key)

Liiteasiakirjan tiedoston hakeminen liiteasiakirjan avaimella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /plan
# See configuration.py for a list of all supported configuration parameters.
configuration = ryhti_api_client.Configuration(
    host = "/plan"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ryhti_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ryhti_api_client.PlanAttachmentDocumentApi(api_client)
    attachment_document_key = 'attachment_document_key_example' # str | Liiteasiakirjan avain

    try:
        # Liiteasiakirjan tiedoston hakeminen liiteasiakirjan avaimella.
        api_response = api_instance.api_plan_attachment_document_attachment_document_key_file_get(attachment_document_key)
        print("The response of PlanAttachmentDocumentApi->api_plan_attachment_document_attachment_document_key_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanAttachmentDocumentApi->api_plan_attachment_document_attachment_document_key_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_document_key** | **str**| Liiteasiakirjan avain | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/tiff

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

