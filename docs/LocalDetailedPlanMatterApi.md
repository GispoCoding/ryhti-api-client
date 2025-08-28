# ryhti_api_client.LocalDetailedPlanMatterApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_local_detailed_plan_matter_permanent_plan_identifier_get**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_get) | **GET** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier} | Kaava-asian (asemakaava) hakeminen pysyvällä kaavatunnuksella.
[**api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get) | **GET** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier}/phase/{planMatterPhaseKey} | Kaava-asian vaiheen (asemakaava) hakeminen vaiheen avaimella.
[**api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post) | **POST** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier}/phase/{planMatterPhaseKey} | Rajapinta uuden vaiheen lisäämiseen olemassa olevalle kaava-asialle (asemakaava).
[**api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put) | **PUT** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier}/phase/{planMatterPhaseKey} | Rajapinta jo tallennetun vaiheen (asemakaava) päivittämiseen.
[**api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post) | **POST** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier}/phase/{planMatterPhaseKey}/validate | Rajapinta uuden kaava-asian (asemakaava) vaiheen validoimiseen ilman tallentamista .
[**api_local_detailed_plan_matter_permanent_plan_identifier_post**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_post) | **POST** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier} | Rajapinta kaava-asian (asemakaava) luomiseen.
[**api_local_detailed_plan_matter_permanent_plan_identifier_post_0**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_post_0) | **POST** /api/LocalDetailedPlanMatter/PermanentPlanIdentifier | Rajapinta asemakaavojen pysyvien ihmisluettavien tunnusten varaamiseen.
[**api_local_detailed_plan_matter_permanent_plan_identifier_put**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_put) | **PUT** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier} | Rajapinta kaava-asian (asemakaava) päivittämiseen.
[**api_local_detailed_plan_matter_permanent_plan_identifier_validate_post**](LocalDetailedPlanMatterApi.md#api_local_detailed_plan_matter_permanent_plan_identifier_validate_post) | **POST** /api/LocalDetailedPlanMatter/{permanentPlanIdentifier}/Validate | Rajapinta kaava-asian (asemakaava) validoimiseen ilman tallentamista.


# **api_local_detailed_plan_matter_permanent_plan_identifier_get**
> PlanMatterResponse api_local_detailed_plan_matter_permanent_plan_identifier_get(permanent_plan_identifier)

Kaava-asian (asemakaava) hakeminen pysyvällä kaavatunnuksella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_response import PlanMatterResponse
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | 

    try:
        # Kaava-asian (asemakaava) hakeminen pysyvällä kaavatunnuksella.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_get(permanent_plan_identifier)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**|  | 

### Return type

[**PlanMatterResponse**](PlanMatterResponse.md)

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

# **api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get**
> PlanMatterPhaseResponse api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get(permanent_plan_identifier, plan_matter_phase_key)

Kaava-asian vaiheen (asemakaava) hakeminen vaiheen avaimella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_phase_response import PlanMatterPhaseResponse
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | 
    plan_matter_phase_key = 'plan_matter_phase_key_example' # str | 

    try:
        # Kaava-asian vaiheen (asemakaava) hakeminen vaiheen avaimella.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get(permanent_plan_identifier, plan_matter_phase_key)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**|  | 
 **plan_matter_phase_key** | **str**|  | 

### Return type

[**PlanMatterPhaseResponse**](PlanMatterPhaseResponse.md)

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
**404** | Resurssia ei löydy. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)

Rajapinta uuden vaiheen lisäämiseen olemassa olevalle kaava-asialle (asemakaava).

Kaava-asia täytyy olla jo lisättynä järjestelmään. Uusi vaihe lisätään edellisen perään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_phase import PlanMatterPhase
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Pysyvä yksilöivä tunnus kaava-asialle.
    plan_matter_phase_key = 'plan_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus kaava-asian vaiheelle.
    plan_matter_phase = ryhti_api_client.PlanMatterPhase() # PlanMatterPhase | Lisättävä kaava-asian vaihe kokonaisuudessaan.

    try:
        # Rajapinta uuden vaiheen lisäämiseen olemassa olevalle kaava-asialle (asemakaava).
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Pysyvä yksilöivä tunnus kaava-asialle. | 
 **plan_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus kaava-asian vaiheelle. | 
 **plan_matter_phase** | [**PlanMatterPhase**](PlanMatterPhase.md)| Lisättävä kaava-asian vaihe kokonaisuudessaan. | 

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
**201** | Kaava-asian vaihe tallennettu. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)

Rajapinta jo tallennetun vaiheen (asemakaava) päivittämiseen.

Kaava-asian vaiheen täytyy olla jo lisättynä järjestelmään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_phase import PlanMatterPhase
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Pysyvä yksilöivä tunnus kaava-asialle.
    plan_matter_phase_key = 'plan_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus kaava-asian vaiheelle.
    plan_matter_phase = ryhti_api_client.PlanMatterPhase() # PlanMatterPhase | Päivitettävä kaava-asian vaihe kokonaisuudessaan.

    try:
        # Rajapinta jo tallennetun vaiheen (asemakaava) päivittämiseen.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Pysyvä yksilöivä tunnus kaava-asialle. | 
 **plan_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus kaava-asian vaiheelle. | 
 **plan_matter_phase** | [**PlanMatterPhase**](PlanMatterPhase.md)| Päivitettävä kaava-asian vaihe kokonaisuudessaan. | 

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
**200** | Kaava-asian vaihe päivitetty. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |
**404** | Resurssia ei löydy. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)

Rajapinta uuden kaava-asian (asemakaava) vaiheen validoimiseen ilman tallentamista .

Kaava-asia täytyy olla jo lisättynä järjestelmään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_phase import PlanMatterPhase
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Pysyvä yksilöivä tunnus kaava-asialle.
    plan_matter_phase_key = 'plan_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus kaava-asian vaiheelle.
    plan_matter_phase = ryhti_api_client.PlanMatterPhase() # PlanMatterPhase | Validoitava kaava-asian vaihe kokonaisuudessaan.

    try:
        # Rajapinta uuden kaava-asian (asemakaava) vaiheen validoimiseen ilman tallentamista .
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post(permanent_plan_identifier, plan_matter_phase_key, plan_matter_phase)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_phase_plan_matter_phase_key_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Pysyvä yksilöivä tunnus kaava-asialle. | 
 **plan_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus kaava-asian vaiheelle. | 
 **plan_matter_phase** | [**PlanMatterPhase**](PlanMatterPhase.md)| Validoitava kaava-asian vaihe kokonaisuudessaan. | 

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
**200** | Kaava-asiassa vaiheessa ei virheitä. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_post**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_post(permanent_plan_identifier, plan_matter_create)

Rajapinta kaava-asian (asemakaava) luomiseen.

Asialle on varattava pysyvä yksilöivä tunnus ennen asian tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla Asemakaavan pysyvätunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_create import PlanMatterCreate
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Pysyvä yksilöivä tunnus kaava-asialle.
    plan_matter_create = ryhti_api_client.PlanMatterCreate() # PlanMatterCreate | Tallennettava kaava-asia sisältäen ensimmäisen kaava-asian vaiheen.

    try:
        # Rajapinta kaava-asian (asemakaava) luomiseen.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_post(permanent_plan_identifier, plan_matter_create)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Pysyvä yksilöivä tunnus kaava-asialle. | 
 **plan_matter_create** | [**PlanMatterCreate**](PlanMatterCreate.md)| Tallennettava kaava-asia sisältäen ensimmäisen kaava-asian vaiheen. | 

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
**201** | Kaava-asia tallennettu. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_post_0**
> str api_local_detailed_plan_matter_permanent_plan_identifier_post_0(reserve_local_detailed_plan_matter_permanent_identifier_command)

Rajapinta asemakaavojen pysyvien ihmisluettavien tunnusten varaamiseen.

Endpoint on idempotentti. Voit kutsua rajapintaa useita kertoja samoilla parametreilla, ja se palauttaa saman tunnisteen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.reserve_local_detailed_plan_matter_permanent_identifier_command import ReserveLocalDetailedPlanMatterPermanentIdentifierCommand
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    reserve_local_detailed_plan_matter_permanent_identifier_command = ryhti_api_client.ReserveLocalDetailedPlanMatterPermanentIdentifierCommand() # ReserveLocalDetailedPlanMatterPermanentIdentifierCommand | Tiedot jotka tarvitaan pysyvän kaavatunnuksen varaamiseen.

    try:
        # Rajapinta asemakaavojen pysyvien ihmisluettavien tunnusten varaamiseen.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_post_0(reserve_local_detailed_plan_matter_permanent_identifier_command)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_local_detailed_plan_matter_permanent_identifier_command** | [**ReserveLocalDetailedPlanMatterPermanentIdentifierCommand**](ReserveLocalDetailedPlanMatterPermanentIdentifierCommand.md)| Tiedot jotka tarvitaan pysyvän kaavatunnuksen varaamiseen. | 

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
**200** | Pysyvä kaavatunnus oli jo olemassa. |  -  |
**201** | Pysyvä kaavatunnus luotiin. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_put**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_put(permanent_plan_identifier, plan_matter_update)

Rajapinta kaava-asian (asemakaava) päivittämiseen.

Rajapinnalla voi päivittää kaava-asian tietoja. Pysyvää kaavatunnusta, hallinnollisen alueen tunnusta ja kaava-asian vaiheita ei voi päivittää tällä rajapinnalla.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_update import PlanMatterUpdate
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Päivitettävän kaava-asian yksilöivä tunnus.
    plan_matter_update = ryhti_api_client.PlanMatterUpdate() # PlanMatterUpdate | Päivitetty kaava-asia ilman kaava-asian vaiheita (planMatterPhases).

    try:
        # Rajapinta kaava-asian (asemakaava) päivittämiseen.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_put(permanent_plan_identifier, plan_matter_update)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Päivitettävän kaava-asian yksilöivä tunnus. | 
 **plan_matter_update** | [**PlanMatterUpdate**](PlanMatterUpdate.md)| Päivitetty kaava-asia ilman kaava-asian vaiheita (planMatterPhases). | 

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
**200** | Kaava-asia päivitetty. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |
**404** | Resurssia ei löydy. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_detailed_plan_matter_permanent_plan_identifier_validate_post**
> SuccessResponse api_local_detailed_plan_matter_permanent_plan_identifier_validate_post(permanent_plan_identifier, plan_matter_create)

Rajapinta kaava-asian (asemakaava) validoimiseen ilman tallentamista.

Rajapinta validoi kaava-asian kokonaisuudessaan, sisältäen ensimmäisen vaiheen ja kaikki sen tiedot.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.plan_matter_create import PlanMatterCreate
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
    api_instance = ryhti_api_client.LocalDetailedPlanMatterApi(api_client)
    permanent_plan_identifier = 'permanent_plan_identifier_example' # str | Pysyvä yksilöivä tunnus kaava-asialle.
    plan_matter_create = ryhti_api_client.PlanMatterCreate() # PlanMatterCreate | Validoitava kaava-asia sisältäen ensimmäisen kaava-asian vaiheen.

    try:
        # Rajapinta kaava-asian (asemakaava) validoimiseen ilman tallentamista.
        api_response = api_instance.api_local_detailed_plan_matter_permanent_plan_identifier_validate_post(permanent_plan_identifier, plan_matter_create)
        print("The response of LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalDetailedPlanMatterApi->api_local_detailed_plan_matter_permanent_plan_identifier_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_plan_identifier** | **str**| Pysyvä yksilöivä tunnus kaava-asialle. | 
 **plan_matter_create** | [**PlanMatterCreate**](PlanMatterCreate.md)| Validoitava kaava-asia sisältäen ensimmäisen kaava-asian vaiheen. | 

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
**200** | Kaava-asiassa ei virheitä. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

