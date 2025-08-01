# ryhti_api_client.AuthenticationApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authenticate_post**](AuthenticationApi.md#api_authenticate_post) | **POST** /api/Authenticate | Hae OAuth2 -token käyttäen client credentials tunnusta ja salaisuutta.


# **api_authenticate_post**
> str api_authenticate_post(client_id=client_id, body=body)

Hae OAuth2 -token käyttäen client credentials tunnusta ja salaisuutta.

ClientId välitetään querysting parametrina ja clientSecrect http bodyssä. <b>X-Token-Expires-In</b> http headerissa palautuu tokenin voimassaoloaika sekunneissa.

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
    api_instance = ryhti_api_client.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | OAuth clientId. (optional)
    body = 'body_example' # str | OAuth clientSecret välitetään http bodyssä heittomerkkien sisällä. Esim. ```\"minunsalaisuus\"``` (optional)

    try:
        # Hae OAuth2 -token käyttäen client credentials tunnusta ja salaisuutta.
        api_response = api_instance.api_authenticate_post(client_id=client_id, body=body)
        print("The response of AuthenticationApi->api_authenticate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_authenticate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| OAuth clientId. | [optional] 
 **body** | **str**| OAuth clientSecret välitetään http bodyssä heittomerkkien sisällä. Esim. &#x60;&#x60;&#x60;\&quot;minunsalaisuus\&quot;&#x60;&#x60;&#x60; | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth token, joka pitää välittää Authorization headerissä muissa api-kutsuissa.              &#x60;&#x60;&#x60;X-Token-Expires-In&#x60;&#x60;&#x60; http header kertoo sekunneissa tokeninen voimassaoloajan.              Muita api-rajapintoja kutsuttaessa lisää kutsuun Authorization header seuraavasti: &#x60;&#x60;&#x60;Authorization: Bearer [token]&#x60;&#x60;&#x60; |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

