# ryhti_api_client.UploadedFileApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_file_post**](UploadedFileApi.md#api_file_post) | **POST** /api/File | 


# **api_file_post**
> str api_file_post(file, municipality_id=municipality_id, region_id=region_id)

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
    api_instance = ryhti_api_client.UploadedFileApi(api_client)
    file = None # bytearray | 
    municipality_id = 'municipality_id_example' # str | Jos käyttäjällä on oikeus useampaan kuntaan tulee pyynnön sisältää kuntaId, jolle tiedosto tuodaan. Vain toinen id on sallittu. (optional)
    region_id = 'region_id_example' # str | Jos käyttäjällä on oikeus useampaan maakuntaan tulee pyynnön sisältää maakuntaId, jolle tiedosto tuodaan. Vain toinen id on sallittu. (optional)

    try:
        api_response = api_instance.api_file_post(file, municipality_id=municipality_id, region_id=region_id)
        print("The response of UploadedFileApi->api_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadedFileApi->api_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **municipality_id** | **str**| Jos käyttäjällä on oikeus useampaan kuntaan tulee pyynnön sisältää kuntaId, jolle tiedosto tuodaan. Vain toinen id on sallittu. | [optional] 
 **region_id** | **str**| Jos käyttäjällä on oikeus useampaan maakuntaan tulee pyynnön sisältää maakuntaId, jolle tiedosto tuodaan. Vain toinen id on sallittu. | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

