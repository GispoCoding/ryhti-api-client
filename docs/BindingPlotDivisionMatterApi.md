# ryhti_api_client.BindingPlotDivisionMatterApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get) | **GET** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier} | Sitovan tonttijaon asian hakeminen pysyvällä sitovan tonttijaon tunnuksella.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get) | **GET** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/phase/{bindingPlotDivisionMatterPhaseKey} | Sitovan tonttijaon asian vaiheen hakeminen avaimella.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post) | **POST** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/phase/{bindingPlotDivisionMatterPhaseKey} | Rajapinta sitovan tonttijaon asian vaiheen lisäämiseen olemassa olevalle sitovan tonttijaon asialle.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put) | **PUT** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/phase/{bindingPlotDivisionMatterPhaseKey} | Rajapinta jo tallennetun vaiheen päivittämiseen.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post) | **POST** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/phase/{bindingPlotDivisionMatterPhaseKey}/validate | Rajapinta sitovan tonttijaon asian vaiheen validoimiseen ilman tallennusta.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post) | **POST** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/planEffects | Rajapinta kaavan vaikutusten luomiseen.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post) | **POST** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier} | Rajapinta sitovan tonttijaon asian luomiseen.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0) | **POST** /api/BindingPlotDivisionMatter/PermanentBindingPlotDivisionIdentifier | Rajapinta sitovan tonttijaon pysyvän tunnuksen varaamiseen.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put) | **PUT** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier} | Rajapinta sitovan tonttijaon asian päivittämiseen.
[**api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post**](BindingPlotDivisionMatterApi.md#api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post) | **POST** /api/BindingPlotDivisionMatter/{permanentBindingPlotDivisionIdentifier}/Validate | Rajapinta sitovan tonttijaon asian validoimiseen ilman tallentamista.


# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get**
> BindingPlotDivisionMatterResponse api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get(permanent_binding_plot_division_identifier)

Sitovan tonttijaon asian hakeminen pysyvällä sitovan tonttijaon tunnuksella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_response import BindingPlotDivisionMatterResponse
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | 

    try:
        # Sitovan tonttijaon asian hakeminen pysyvällä sitovan tonttijaon tunnuksella.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get(permanent_binding_plot_division_identifier)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**|  | 

### Return type

[**BindingPlotDivisionMatterResponse**](BindingPlotDivisionMatterResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get**
> BindingPlotDivisionMatterPhase api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key)

Sitovan tonttijaon asian vaiheen hakeminen avaimella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_phase import BindingPlotDivisionMatterPhase
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | 
    binding_plot_division_matter_phase_key = 'binding_plot_division_matter_phase_key_example' # str | 

    try:
        # Sitovan tonttijaon asian vaiheen hakeminen avaimella.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**|  | 
 **binding_plot_division_matter_phase_key** | **str**|  | 

### Return type

[**BindingPlotDivisionMatterPhase**](BindingPlotDivisionMatterPhase.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post**
> SuccessResponse api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)

Rajapinta sitovan tonttijaon asian vaiheen lisäämiseen olemassa olevalle sitovan tonttijaon asialle.

Sitovan tonttijaon asian täytyy olla jo lisättynä järjestelmään. Uusi vaihe lisätään edellisen perään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_phase import BindingPlotDivisionMatterPhase
from ryhti_api_client.models.success_response import SuccessResponse
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle.
    binding_plot_division_matter_phase_key = 'binding_plot_division_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus sitovan tonttijaon asian vaiheelle.
    binding_plot_division_matter_phase = ryhti_api_client.BindingPlotDivisionMatterPhase() # BindingPlotDivisionMatterPhase | Lisättävä sitovan tonttijaon asian vaihe kokonaisuudessaan.

    try:
        # Rajapinta sitovan tonttijaon asian vaiheen lisäämiseen olemassa olevalle sitovan tonttijaon asialle.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**| Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle. | 
 **binding_plot_division_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus sitovan tonttijaon asian vaiheelle. | 
 **binding_plot_division_matter_phase** | [**BindingPlotDivisionMatterPhase**](BindingPlotDivisionMatterPhase.md)| Lisättävä sitovan tonttijaon asian vaihe kokonaisuudessaan. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sitovan tonttijaon asian vaihe tallennettu. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put**
> api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)

Rajapinta jo tallennetun vaiheen päivittämiseen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_phase import BindingPlotDivisionMatterPhase
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | 
    binding_plot_division_matter_phase_key = 'binding_plot_division_matter_phase_key_example' # str | 
    binding_plot_division_matter_phase = ryhti_api_client.BindingPlotDivisionMatterPhase() # BindingPlotDivisionMatterPhase | 

    try:
        # Rajapinta jo tallennetun vaiheen päivittämiseen.
        api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**|  | 
 **binding_plot_division_matter_phase_key** | **str**|  | 
 **binding_plot_division_matter_phase** | [**BindingPlotDivisionMatterPhase**](BindingPlotDivisionMatterPhase.md)|  | 

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
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**404** | Resurssia ei löydy. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |
**200** | Vaihe päivitetty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post**
> SuccessResponse api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)

Rajapinta sitovan tonttijaon asian vaiheen validoimiseen ilman tallennusta.

Sitovan tonttijaon asian täytyy olla jo lisättynä järjestelmään. Uusi vaihe lisätään edellisen perään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_phase import BindingPlotDivisionMatterPhase
from ryhti_api_client.models.success_response import SuccessResponse
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle.
    binding_plot_division_matter_phase_key = 'binding_plot_division_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus sitovan tonttijaon asian vaiheelle.
    binding_plot_division_matter_phase = ryhti_api_client.BindingPlotDivisionMatterPhase() # BindingPlotDivisionMatterPhase | Lisättävä sitovan tonttijaon asian vaihe kokonaisuudessaan.

    try:
        # Rajapinta sitovan tonttijaon asian vaiheen validoimiseen ilman tallennusta.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_phase_key, binding_plot_division_matter_phase)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_phase_binding_plot_division_matter_phase_key_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**| Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle. | 
 **binding_plot_division_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus sitovan tonttijaon asian vaiheelle. | 
 **binding_plot_division_matter_phase** | [**BindingPlotDivisionMatterPhase**](BindingPlotDivisionMatterPhase.md)| Lisättävä sitovan tonttijaon asian vaihe kokonaisuudessaan. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vaiheessa ei virheitä. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post**
> str api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post(permanent_binding_plot_division_identifier, plan_effects)

Rajapinta kaavan vaikutusten luomiseen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_effects import PlanEffects
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | Pysyvä yksilöivä tunnus sitovan tonttijaon asialle.
    plan_effects = ryhti_api_client.PlanEffects() # PlanEffects | Kaavan vaikutukset.

    try:
        # Rajapinta kaavan vaikutusten luomiseen.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post(permanent_binding_plot_division_identifier, plan_effects)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_plan_effects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**| Pysyvä yksilöivä tunnus sitovan tonttijaon asialle. | 
 **plan_effects** | [**PlanEffects**](PlanEffects.md)| Kaavan vaikutukset. | 

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
**201** | Kaavan vaikutukset tallennettu, paluuarvona uri tallennettuun resurssiin. |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post**
> str api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_create)

Rajapinta sitovan tonttijaon asian luomiseen.

Asialle on varattava pysyvä yksilöivä tunnus ennen asian tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla sitovan tonttijaon pysyvä tunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_create import BindingPlotDivisionMatterCreate
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | Pysyvä yksilöivä tunnus sitovan tonttijaon asialle.
    binding_plot_division_matter_create = ryhti_api_client.BindingPlotDivisionMatterCreate() # BindingPlotDivisionMatterCreate | Sitovan tonttijaon asia.

    try:
        # Rajapinta sitovan tonttijaon asian luomiseen.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_create)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**| Pysyvä yksilöivä tunnus sitovan tonttijaon asialle. | 
 **binding_plot_division_matter_create** | [**BindingPlotDivisionMatterCreate**](BindingPlotDivisionMatterCreate.md)| Sitovan tonttijaon asia. | 

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
**201** | Sitovan tonttijaon asia tallennettu, paluuarvona uri tallennettuun resurssiin. |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0**
> str api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0(reserve_permanent_binding_plot_division_identifier_command)

Rajapinta sitovan tonttijaon pysyvän tunnuksen varaamiseen.

Endpoint on idempotentti. Voit kutsua rajapintaa useita kertoja samoilla parametreilla, ja se palauttaa saman tunnisteen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.reserve_permanent_binding_plot_division_identifier_command import ReservePermanentBindingPlotDivisionIdentifierCommand
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    reserve_permanent_binding_plot_division_identifier_command = ryhti_api_client.ReservePermanentBindingPlotDivisionIdentifierCommand() # ReservePermanentBindingPlotDivisionIdentifierCommand | Tiedot jotka tarvitaan pysyvän tunnuksen varaamiseen.

    try:
        # Rajapinta sitovan tonttijaon pysyvän tunnuksen varaamiseen.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0(reserve_permanent_binding_plot_division_identifier_command)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_permanent_binding_plot_division_identifier_command** | [**ReservePermanentBindingPlotDivisionIdentifierCommand**](ReservePermanentBindingPlotDivisionIdentifierCommand.md)| Tiedot jotka tarvitaan pysyvän tunnuksen varaamiseen. | 

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
**200** | Pysyvä sitovan tonttijaon tunnus oli jo olemassa. |  -  |
**201** | Pysyvä sitovan tonttijaon tunnus luotiin. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put**
> api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put(permanent_binding_plot_division_identifier, binding_plot_division_matter_update)

Rajapinta sitovan tonttijaon asian päivittämiseen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_update import BindingPlotDivisionMatterUpdate
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | 
    binding_plot_division_matter_update = ryhti_api_client.BindingPlotDivisionMatterUpdate() # BindingPlotDivisionMatterUpdate | 

    try:
        # Rajapinta sitovan tonttijaon asian päivittämiseen.
        api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put(permanent_binding_plot_division_identifier, binding_plot_division_matter_update)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**|  | 
 **binding_plot_division_matter_update** | [**BindingPlotDivisionMatterUpdate**](BindingPlotDivisionMatterUpdate.md)|  | 

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
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**404** | Resurssia ei löydy. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |
**200** | Asia päivitetty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post**
> SuccessResponse api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_create)

Rajapinta sitovan tonttijaon asian validoimiseen ilman tallentamista.

Rajapinta validoi sitovan tonttijaon asian kokonaisuudessaan, sisältäen ensimmäisen vaiheen ja kaikki sen tiedot.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.binding_plot_division_matter_create import BindingPlotDivisionMatterCreate
from ryhti_api_client.models.success_response import SuccessResponse
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
    api_instance = ryhti_api_client.BindingPlotDivisionMatterApi(api_client)
    permanent_binding_plot_division_identifier = 'permanent_binding_plot_division_identifier_example' # str | Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle.
    binding_plot_division_matter_create = ryhti_api_client.BindingPlotDivisionMatterCreate() # BindingPlotDivisionMatterCreate | Validoitava sitovan tonttijaon asian sisältäen ensimmäisen sitovan tonttijaon asian vaiheen.

    try:
        # Rajapinta sitovan tonttijaon asian validoimiseen ilman tallentamista.
        api_response = api_instance.api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post(permanent_binding_plot_division_identifier, binding_plot_division_matter_create)
        print("The response of BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingPlotDivisionMatterApi->api_binding_plot_division_matter_permanent_binding_plot_division_identifier_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_binding_plot_division_identifier** | **str**| Pysyvä sitovan tonttijaon tunnus sitovan tonttijaon asialle. | 
 **binding_plot_division_matter_create** | [**BindingPlotDivisionMatterCreate**](BindingPlotDivisionMatterCreate.md)| Validoitava sitovan tonttijaon asian sisältäen ensimmäisen sitovan tonttijaon asian vaiheen. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sitovan tonttijaon asiassa ei virheitä. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

