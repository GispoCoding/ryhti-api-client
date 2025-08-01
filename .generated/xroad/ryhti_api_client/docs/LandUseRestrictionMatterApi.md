# ryhti_api_client.LandUseRestrictionMatterApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get) | **GET** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier} | Alueidenkäytön rajoituksen asia hakeminen pysyvän yksilöivän tunnuksen perusteella.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get) | **GET** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier}/phase/{landUseRestrictionMatterPhaseKey} | Alueidenkäytön rajoituksen vaiheen hakeminen avaimella.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post) | **POST** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier}/phase/{landUseRestrictionMatterPhaseKey} | Rajapinta uuden vaiheen lisäämiseen olemassa olevalle alueidenkäytön rajoituksen asialle.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put) | **PUT** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier}/phase/{landUseRestrictionMatterPhaseKey} | Rajapinta jo tallennetun vaiheen päivittämiseen.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post) | **POST** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier}/phase/{landUseRestrictionMatterPhaseKey}/validate | Rajapinta uuden vaiheen validoimiseen ilman tallennusta.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post) | **POST** /api/LandUseRestrictionMatter/PermanentLandUseRestrictionIdentifier | Rajapinta alueidenkäytön rajoitusten pysyvän tunnuksen varaamiseen.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0) | **POST** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier} | Rajapinta alueidenkäytön rajoituksen asian luomiseen.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put) | **PUT** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier} | Rajapinta alueidenkäytön rajoituksen asian päivittämiseen.
[**api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post**](LandUseRestrictionMatterApi.md#api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post) | **POST** /api/LandUseRestrictionMatter/{permanentLandUseRestrictionIdentifier}/Validate | Rajapinta alueidenkäytön rajoituksen asian validoimiseen ilman tallentamista.


# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get**
> LandUseRestrictionMatterResponse api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get(permanent_land_use_restriction_identifier)

Alueidenkäytön rajoituksen asia hakeminen pysyvän yksilöivän tunnuksen perusteella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_response import LandUseRestrictionMatterResponse
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | Alueidenkäytön rajoituksen pysyvä tunnus

    try:
        # Alueidenkäytön rajoituksen asia hakeminen pysyvän yksilöivän tunnuksen perusteella.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get(permanent_land_use_restriction_identifier)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**| Alueidenkäytön rajoituksen pysyvä tunnus | 

### Return type

[**LandUseRestrictionMatterResponse**](LandUseRestrictionMatterResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alueidenkäytön rajoituksen asia JSON-oliona |  -  |
**404** | Pysyvällä yksilöivällä tunnuksella ei löydy tallennettau alueidenkäytön rajoituksen asia. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get**
> LandUseRestrictionMatterPhase api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key)

Alueidenkäytön rajoituksen vaiheen hakeminen avaimella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_phase import LandUseRestrictionMatterPhase
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | 
    land_use_restriction_matter_phase_key = 'land_use_restriction_matter_phase_key_example' # str | 

    try:
        # Alueidenkäytön rajoituksen vaiheen hakeminen avaimella.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**|  | 
 **land_use_restriction_matter_phase_key** | **str**|  | 

### Return type

[**LandUseRestrictionMatterPhase**](LandUseRestrictionMatterPhase.md)

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

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post**
> SuccessResponse api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)

Rajapinta uuden vaiheen lisäämiseen olemassa olevalle alueidenkäytön rajoituksen asialle.

Alueidenkäytön rajoituksen asia täytyy olla jo lisättynä järjestelmään. Uusi vaihe lisätään edellisen perään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_phase import LandUseRestrictionMatterPhase
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asia.
    land_use_restriction_matter_phase_key = 'land_use_restriction_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus vaiheelle.
    land_use_restriction_matter_phase = ryhti_api_client.LandUseRestrictionMatterPhase() # LandUseRestrictionMatterPhase | Lisättävä vaihe kokonaisuudessaan.

    try:
        # Rajapinta uuden vaiheen lisäämiseen olemassa olevalle alueidenkäytön rajoituksen asialle.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**| Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asia. | 
 **land_use_restriction_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus vaiheelle. | 
 **land_use_restriction_matter_phase** | [**LandUseRestrictionMatterPhase**](LandUseRestrictionMatterPhase.md)| Lisättävä vaihe kokonaisuudessaan. | 

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
**201** | Vaihe tallennettu. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put**
> api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)

Rajapinta jo tallennetun vaiheen päivittämiseen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_phase import LandUseRestrictionMatterPhase
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | 
    land_use_restriction_matter_phase_key = 'land_use_restriction_matter_phase_key_example' # str | 
    land_use_restriction_matter_phase = ryhti_api_client.LandUseRestrictionMatterPhase() # LandUseRestrictionMatterPhase | 

    try:
        # Rajapinta jo tallennetun vaiheen päivittämiseen.
        api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**|  | 
 **land_use_restriction_matter_phase_key** | **str**|  | 
 **land_use_restriction_matter_phase** | [**LandUseRestrictionMatterPhase**](LandUseRestrictionMatterPhase.md)|  | 

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

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post**
> SuccessResponse api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)

Rajapinta uuden vaiheen validoimiseen ilman tallennusta.

Alueidenkäytön rajoituksen asia täytyy olla jo lisättynä järjestelmään. Uusi vaihe lisätään edellisen perään.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_phase import LandUseRestrictionMatterPhase
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asia.
    land_use_restriction_matter_phase_key = 'land_use_restriction_matter_phase_key_example' # str | Pysyvä yksilöivä tunnus vaiheelle.
    land_use_restriction_matter_phase = ryhti_api_client.LandUseRestrictionMatterPhase() # LandUseRestrictionMatterPhase | Lisättävä vaihe kokonaisuudessaan.

    try:
        # Rajapinta uuden vaiheen validoimiseen ilman tallennusta.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_phase_key, land_use_restriction_matter_phase)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_phase_land_use_restriction_matter_phase_key_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**| Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asia. | 
 **land_use_restriction_matter_phase_key** | **str**| Pysyvä yksilöivä tunnus vaiheelle. | 
 **land_use_restriction_matter_phase** | [**LandUseRestrictionMatterPhase**](LandUseRestrictionMatterPhase.md)| Lisättävä vaihe kokonaisuudessaan. | 

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

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post**
> str api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post(reserve_permanent_land_use_restriction_identifier_command)

Rajapinta alueidenkäytön rajoitusten pysyvän tunnuksen varaamiseen.

Endpoint on idempotentti. Voit kutsua rajapintaa useita kertoja samoilla parametreilla, ja se palauttaa saman tunnisteen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.reserve_permanent_land_use_restriction_identifier_command import ReservePermanentLandUseRestrictionIdentifierCommand
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    reserve_permanent_land_use_restriction_identifier_command = ryhti_api_client.ReservePermanentLandUseRestrictionIdentifierCommand() # ReservePermanentLandUseRestrictionIdentifierCommand | Tiedot jotka tarvitaan pysyvän tunnuksen varaamiseen.

    try:
        # Rajapinta alueidenkäytön rajoitusten pysyvän tunnuksen varaamiseen.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post(reserve_permanent_land_use_restriction_identifier_command)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_permanent_land_use_restriction_identifier_command** | [**ReservePermanentLandUseRestrictionIdentifierCommand**](ReservePermanentLandUseRestrictionIdentifierCommand.md)| Tiedot jotka tarvitaan pysyvän tunnuksen varaamiseen. | 

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
**200** | Pysyvä alueidenkäytön rajoituksen tunnus oli jo olemassa. |  -  |
**201** | Pysyvä alueidenkäytön rajoituksen tunnus luotiin. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0**
> SuccessResponse api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0(permanent_land_use_restriction_identifier, land_use_restriction_matter_create)

Rajapinta alueidenkäytön rajoituksen asian luomiseen.

Asialle on varattava pysyvä yksilöivä tunnus ennen asian tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla alueidenkäytön rajoituksen pysyvä tunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_create import LandUseRestrictionMatterCreate
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asialle.
    land_use_restriction_matter_create = ryhti_api_client.LandUseRestrictionMatterCreate() # LandUseRestrictionMatterCreate | Alueidenkäytön rajoituksen asia.

    try:
        # Rajapinta alueidenkäytön rajoituksen asian luomiseen.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0(permanent_land_use_restriction_identifier, land_use_restriction_matter_create)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**| Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asialle. | 
 **land_use_restriction_matter_create** | [**LandUseRestrictionMatterCreate**](LandUseRestrictionMatterCreate.md)| Alueidenkäytön rajoituksen asia. | 

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
**201** | Alueidenkäytön rajoituksen asia tallennettu, paluuarvona uri tallennettuun resurssiin. |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put**
> api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put(permanent_land_use_restriction_identifier, land_use_restriction_matter_update)

Rajapinta alueidenkäytön rajoituksen asian päivittämiseen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_update import LandUseRestrictionMatterUpdate
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | 
    land_use_restriction_matter_update = ryhti_api_client.LandUseRestrictionMatterUpdate() # LandUseRestrictionMatterUpdate | 

    try:
        # Rajapinta alueidenkäytön rajoituksen asian päivittämiseen.
        api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put(permanent_land_use_restriction_identifier, land_use_restriction_matter_update)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**|  | 
 **land_use_restriction_matter_update** | [**LandUseRestrictionMatterUpdate**](LandUseRestrictionMatterUpdate.md)|  | 

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

# **api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post**
> SuccessResponse api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_create)

Rajapinta alueidenkäytön rajoituksen asian validoimiseen ilman tallentamista.

Asialle on varattava pysyvä yksilöivä tunnus ennen asian tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla alueidenkäytön rajoituksen pysyvä tunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.land_use_restriction_matter_create import LandUseRestrictionMatterCreate
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
    api_instance = ryhti_api_client.LandUseRestrictionMatterApi(api_client)
    permanent_land_use_restriction_identifier = 'permanent_land_use_restriction_identifier_example' # str | Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asialle.
    land_use_restriction_matter_create = ryhti_api_client.LandUseRestrictionMatterCreate() # LandUseRestrictionMatterCreate | Alueidenkäytön rajoituksen asia.

    try:
        # Rajapinta alueidenkäytön rajoituksen asian validoimiseen ilman tallentamista.
        api_response = api_instance.api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post(permanent_land_use_restriction_identifier, land_use_restriction_matter_create)
        print("The response of LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandUseRestrictionMatterApi->api_land_use_restriction_matter_permanent_land_use_restriction_identifier_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_land_use_restriction_identifier** | **str**| Pysyvä yksilöivä tunnus alueidenkäytön rajoituksen asialle. | 
 **land_use_restriction_matter_create** | [**LandUseRestrictionMatterCreate**](LandUseRestrictionMatterCreate.md)| Alueidenkäytön rajoituksen asia. | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |
**201** | Alueidenkäytön rajoituksen asia tallennettu, paluuarvona uri tallennettuun resurssiin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

