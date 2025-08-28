# ryhti_api_client.PlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_plan_validate_post**](PlanApi.md#api_plan_validate_post) | **POST** /api/Plan/Validate | Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.


# **api_plan_validate_post**
> api_plan_validate_post(plan_type, administrative_area_identifiers, plan)

Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan import Plan
from ryhti_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ryhti_api_client.Configuration(
    host = "http://localhost"
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
    api_instance = ryhti_api_client.PlanApi(api_client)
    plan_type = '21' # str | Kaavalaji-koodiston arvo http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji
    administrative_area_identifiers = ['administrative_area_identifiers_example'] # List[str] | Kunta- tai maakuntakoodi.     Esimerkki : 049
    plan = ryhti_api_client.Plan() # Plan | Yksittäinen kaava.

    try:
        # Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.
        api_instance.api_plan_validate_post(plan_type, administrative_area_identifiers, plan)
    except Exception as e:
        print("Exception when calling PlanApi->api_plan_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_type** | **str**| Kaavalaji-koodiston arvo http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji | 
 **administrative_area_identifiers** | [**List[str]**](str.md)| Kunta- tai maakuntakoodi.     Esimerkki : 049 | 
 **plan** | [**Plan**](Plan.md)| Yksittäinen kaava. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kaavassa ei virheitä. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

