# ryhti_api_client.BuildingOrdinanceApi

All URIs are relative to */plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_building_ordinance_permanent_building_ordinance_identifier_get**](BuildingOrdinanceApi.md#api_building_ordinance_permanent_building_ordinance_identifier_get) | **GET** /api/BuildingOrdinance/{permanentBuildingOrdinanceIdentifier} | Rakennusjärjestyksen hakeminen pysyvän yksilöivän tunnuksen perusteella.
[**api_building_ordinance_permanent_building_ordinance_identifier_post**](BuildingOrdinanceApi.md#api_building_ordinance_permanent_building_ordinance_identifier_post) | **POST** /api/BuildingOrdinance/PermanentBuildingOrdinanceIdentifier | Rajapinta rakennusjärjestystunnusten pysyvien ihmisluettavien tunnusten varaamiseen.
[**api_building_ordinance_permanent_building_ordinance_identifier_post_0**](BuildingOrdinanceApi.md#api_building_ordinance_permanent_building_ordinance_identifier_post_0) | **POST** /api/BuildingOrdinance/{permanentBuildingOrdinanceIdentifier} | Rajapinta rakennusjärjestyksen luomiseen.
[**api_building_ordinance_permanent_building_ordinance_identifier_put**](BuildingOrdinanceApi.md#api_building_ordinance_permanent_building_ordinance_identifier_put) | **PUT** /api/BuildingOrdinance/{permanentBuildingOrdinanceIdentifier} | Rajapinta rakennusjärjestyksen päivittämiseen.
[**api_building_ordinance_permanent_building_ordinance_identifier_validate_post**](BuildingOrdinanceApi.md#api_building_ordinance_permanent_building_ordinance_identifier_validate_post) | **POST** /api/BuildingOrdinance/{permanentBuildingOrdinanceIdentifier}/Validate | Rajapinta rakennusjärjestyksen validoimiseen ilman tallentamista.


# **api_building_ordinance_permanent_building_ordinance_identifier_get**
> BuildingOrdinance api_building_ordinance_permanent_building_ordinance_identifier_get(permanent_building_ordinance_identifier)

Rakennusjärjestyksen hakeminen pysyvän yksilöivän tunnuksen perusteella.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.building_ordinance import BuildingOrdinance
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
    api_instance = ryhti_api_client.BuildingOrdinanceApi(api_client)
    permanent_building_ordinance_identifier = 'permanent_building_ordinance_identifier_example' # str | Heattavan rakennusjärjestyksen pysyvä yksilöivä tunnus.

    try:
        # Rakennusjärjestyksen hakeminen pysyvän yksilöivän tunnuksen perusteella.
        api_response = api_instance.api_building_ordinance_permanent_building_ordinance_identifier_get(permanent_building_ordinance_identifier)
        print("The response of BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_building_ordinance_identifier** | **str**| Heattavan rakennusjärjestyksen pysyvä yksilöivä tunnus. | 

### Return type

[**BuildingOrdinance**](BuildingOrdinance.md)

### Authorization

[oauth2](../README.md#oauth2), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rakennusjärjestys JSON-oliona |  -  |
**404** | Pysyvällä yksilöivällä tunnuksella ei löydy tallennettau rakennusjärjestystä. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_building_ordinance_permanent_building_ordinance_identifier_post**
> str api_building_ordinance_permanent_building_ordinance_identifier_post(reserve_building_ordinance_permanent_identifier_command)

Rajapinta rakennusjärjestystunnusten pysyvien ihmisluettavien tunnusten varaamiseen.

Endpoint on idempotentti. Voit kutsua rajapintaa useita kertoja samoilla parametreilla, ja se palauttaa saman tunnisteen.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.reserve_building_ordinance_permanent_identifier_command import ReserveBuildingOrdinancePermanentIdentifierCommand
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
    api_instance = ryhti_api_client.BuildingOrdinanceApi(api_client)
    reserve_building_ordinance_permanent_identifier_command = ryhti_api_client.ReserveBuildingOrdinancePermanentIdentifierCommand() # ReserveBuildingOrdinancePermanentIdentifierCommand | Tiedot jotka tarvitaan pysyvän rakennusjärjestystunnuksen varaamiseen.

    try:
        # Rajapinta rakennusjärjestystunnusten pysyvien ihmisluettavien tunnusten varaamiseen.
        api_response = api_instance.api_building_ordinance_permanent_building_ordinance_identifier_post(reserve_building_ordinance_permanent_identifier_command)
        print("The response of BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_building_ordinance_permanent_identifier_command** | [**ReserveBuildingOrdinancePermanentIdentifierCommand**](ReserveBuildingOrdinancePermanentIdentifierCommand.md)| Tiedot jotka tarvitaan pysyvän rakennusjärjestystunnuksen varaamiseen. | 

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
**200** | Pysyvä rakennusjärjestystunnus oli jo olemassa. |  -  |
**201** | Pysyvä rakennusjärjestystunnus luotiin. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_building_ordinance_permanent_building_ordinance_identifier_post_0**
> str api_building_ordinance_permanent_building_ordinance_identifier_post_0(permanent_building_ordinance_identifier, building_ordinance)

Rajapinta rakennusjärjestyksen luomiseen.

Rakennusjärjestykselle on varattava pysyvä yksilöivä tunnus ennen järjestyksen tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla rakennusjärjestyksen pysyvä tunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.building_ordinance import BuildingOrdinance
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
    api_instance = ryhti_api_client.BuildingOrdinanceApi(api_client)
    permanent_building_ordinance_identifier = 'permanent_building_ordinance_identifier_example' # str | Pysyvä yksilöivä tunnus rakennusjärjestykselle.
    building_ordinance = ryhti_api_client.BuildingOrdinance() # BuildingOrdinance | Rakennusjärjestys.

    try:
        # Rajapinta rakennusjärjestyksen luomiseen.
        api_response = api_instance.api_building_ordinance_permanent_building_ordinance_identifier_post_0(permanent_building_ordinance_identifier, building_ordinance)
        print("The response of BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_building_ordinance_identifier** | **str**| Pysyvä yksilöivä tunnus rakennusjärjestykselle. | 
 **building_ordinance** | [**BuildingOrdinance**](BuildingOrdinance.md)| Rakennusjärjestys. | 

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
**201** | Rakennusjärjestys tallennettu, paluuarvona uri tallennettuun resurssiin. |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_building_ordinance_permanent_building_ordinance_identifier_put**
> SuccessResponse api_building_ordinance_permanent_building_ordinance_identifier_put(permanent_building_ordinance_identifier, building_ordinance)

Rajapinta rakennusjärjestyksen päivittämiseen.

Rajapinnalla voi rakennusjärjestyksen tietoja. Pysyvää tunnusta ja hallinnollisen alueen tunnusta ei voi päivittää.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.building_ordinance import BuildingOrdinance
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
    api_instance = ryhti_api_client.BuildingOrdinanceApi(api_client)
    permanent_building_ordinance_identifier = 'permanent_building_ordinance_identifier_example' # str | Rakennusjärjestyksen pysyvä tunnus.
    building_ordinance = ryhti_api_client.BuildingOrdinance() # BuildingOrdinance | Päivitetty rakennysjärjestys.

    try:
        # Rajapinta rakennusjärjestyksen päivittämiseen.
        api_response = api_instance.api_building_ordinance_permanent_building_ordinance_identifier_put(permanent_building_ordinance_identifier, building_ordinance)
        print("The response of BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_building_ordinance_identifier** | **str**| Rakennusjärjestyksen pysyvä tunnus. | 
 **building_ordinance** | [**BuildingOrdinance**](BuildingOrdinance.md)| Päivitetty rakennysjärjestys. | 

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
**200** | Rakennusjärjestys päivitetty. |  -  |
**400** | Kutsun rakenne ei ole scheman mukainen. |  -  |
**422** | Kutsun tietosisällössä virheitä. |  -  |
**404** | Resurssia ei löydy. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_building_ordinance_permanent_building_ordinance_identifier_validate_post**
> SuccessResponse api_building_ordinance_permanent_building_ordinance_identifier_validate_post(permanent_building_ordinance_identifier, building_ordinance)

Rajapinta rakennusjärjestyksen validoimiseen ilman tallentamista.

Rakennusjärjestykselle on varattava pysyvä yksilöivä tunnus ennen järjestyksen tuontia Ryhtiin. Pysyvän yksilöivän tunnuksen tulee olla rakennusjärjestyksen pysyvä tunnus.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (Bearer):

```python
import ryhti_api_client
from ryhti_api_client.models.building_ordinance import BuildingOrdinance
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
    api_instance = ryhti_api_client.BuildingOrdinanceApi(api_client)
    permanent_building_ordinance_identifier = 'permanent_building_ordinance_identifier_example' # str | Pysyvä yksilöivä tunnus rakennusjärjestykselle.
    building_ordinance = ryhti_api_client.BuildingOrdinance() # BuildingOrdinance | Rakennusjärjestys.

    try:
        # Rajapinta rakennusjärjestyksen validoimiseen ilman tallentamista.
        api_response = api_instance.api_building_ordinance_permanent_building_ordinance_identifier_validate_post(permanent_building_ordinance_identifier, building_ordinance)
        print("The response of BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingOrdinanceApi->api_building_ordinance_permanent_building_ordinance_identifier_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permanent_building_ordinance_identifier** | **str**| Pysyvä yksilöivä tunnus rakennusjärjestykselle. | 
 **building_ordinance** | [**BuildingOrdinance**](BuildingOrdinance.md)| Rakennusjärjestys. | 

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
**200** | Rakennusjärjestyksessä ei virheitä. |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

