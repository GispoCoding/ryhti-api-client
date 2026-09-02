# ryhti_api_client.PlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin**](PlanApi.md#post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin) | **POST** /api/Plan/Validate | Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.


# **post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin**
> post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin(plan_type, administrative_area_identifiers, validate_plan=validate_plan)

Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.

Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import ryhti_api_client
from ryhti_api_client.models.validate_plan import ValidatePlan
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

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with ryhti_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ryhti_api_client.PlanApi(api_client)
    plan_type = '21' # str | Kaavalaji-koodiston arvo http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji
    administrative_area_identifiers = ['administrative_area_identifiers_example'] # List[str] | Kunta- tai maakuntakoodi.     Esimerkki : 049
    validate_plan = {"planKey":"string","planUri":"string","lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","legalEffectOfLocalMasterPlans":["http://uri.suomi.fi/codelist/rytj/oikeusvaik_YK/code/1"],"scale":0,"officialUseOnly":true,"planMaps":[{"planMapKey":"string","planMapUri":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"fileKey":"string","coordinateSystem":"http://uri.suomi.fi/codelist/rakrek/ETRS89/code/EPSG3067"}],"geographicalArea":{"srid":"3067","geometry":{"coordinates":"[100.0, 0.0]","type":"Point"}},"planDescription":"string","planAnnexes":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}],"otherPlanMaterials":[{"otherPlanMaterialKey":"string","otherPlanMaterialUri":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"fileKey":"string","otherPlanMaterialLink":"string","personalDataContent":"string","categoryOfPublicity":"string"}],"planCancellationInfos":[{"planCancellationInfoKey":"string","planCancellationInfoUri":"string","cancelledPlanUri":"string","cancelsEntirePlan":true,"cancelledGroupRelations":[{"planRegulationGroupUri":"string","planObjectUri":"string"}],"planObjectCancellationInfos":[{"planObjectCancellationInfoKey":"string","cancelledPlanObjectUri":"string","cancelsEntirePlanObject":true,"validityGeometry":{"srid":"3067","geometry":{"coordinates":"[100.0, 0.0]","type":"Point"}}}],"cancelledGeneralRegulationGroupUris":["string"]}],"planReport":{"planReportKey":"string","planReportUri":"string","attachmentDocuments":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}]},"generalRegulationGroups":[{"generalRegulationGroupKey":"string","generalRegulationGroupUri":"string","titleOfPlanRegulation":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"planRegulations":[{"planRegulationKey":"string","planRegulationUri":"string","value":{"code":"string","codeList":"string","title":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"dataType":"LocalizedText"},"lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","type":"http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayslaji/code/asumisenAlue","verbalRegulations":["http://uri.suomi.fi/codelist/rytj/RY_Sanallisen_Kaavamaarayksen_Laji/code/rakentamistapa"],"additionalInformations":[{"type":"http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayksen_Lisatiedonlaji/code/tyyppi","value":{"code":"string","codeList":"string","title":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"dataType":"LocalizedText"}}],"relatedDocuments":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}],"planThemes":["string"],"periodOfValidity":{"begin":"string","end":"string"},"subjectIdentifiers":["string"],"regulationNumber":"string"}],"planRecommendations":[{"planRecommendationKey":"string","planRecommendationUri":"string","value":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","relatedDocuments":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}],"planThemes":["string"],"periodOfValidity":{"begin":"string","end":"string"},"recommendationNumber":0}],"groupNumber":0}],"presentationAlignments":[{"planObjectKey":"string","planRegulationGroupKey":"string","geometry":{"srid":"3067","geometry":{"coordinates":"[100.0, 0.0]","type":"Point"}},"rotation":0,"language":"string"}],"periodOfValidity":{"begin":"string","end":"string"},"approvalDate":"string","planners":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"planObjects":[{"planObjectKey":"string","planObjectUri":"string","lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","undergroundStatus":"string","geometry":{"srid":"3067","geometry":{"coordinates":"[100.0, 0.0]","type":"Point"}},"name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"description":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"verticalLimit":{"minimumValue":0,"maximumValue":0,"unitOfMeasure":"string","dataType":"LocalizedText"},"relatedPlanSourceDataKeys":["string"],"relatedPlanSourceDataUris":["string"],"periodOfValidity":{"begin":"string","end":"string"},"objectNumber":0,"relatedPlanObjectKeys":["string"],"relatedPlanObjectUris":["string"]}],"planRegulationGroups":[{"planRegulationGroupKey":"string","planRegulationGroupUri":"string","titleOfPlanRegulation":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"letterIdentifier":"string","planRegulations":[{"planRegulationKey":"string","planRegulationUri":"string","value":{"code":"string","codeList":"string","title":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"dataType":"LocalizedText"},"lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","type":"http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayslaji/code/asumisenAlue","verbalRegulations":["http://uri.suomi.fi/codelist/rytj/RY_Sanallisen_Kaavamaarayksen_Laji/code/rakentamistapa"],"additionalInformations":[{"type":"http://uri.suomi.fi/codelist/rytj/RY_Kaavamaarayksen_Lisatiedonlaji/code/tyyppi","value":{"code":"string","codeList":"string","title":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"dataType":"LocalizedText"}}],"relatedDocuments":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}],"planThemes":["string"],"periodOfValidity":{"begin":"string","end":"string"},"subjectIdentifiers":["string"],"regulationNumber":"string"}],"planRecommendations":[{"planRecommendationKey":"string","planRecommendationUri":"string","value":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"lifeCycleStatus":"http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/01","relatedDocuments":[{"attachmentDocumentKey":"string","documentIdentifier":"string","name":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"personalDataContent":"string","categoryOfPublicity":"string","accessibility":true,"retentionTime":"string","confirmationDate":"string","languages":["string"],"fileKey":"string","descriptors":[{"descriptorIdentifier":"string","vocabulary":"string","descriptor":"string"}],"documentDate":"string","arrivedDate":"string","planAttachmentDocumentUri":"string","typeOfAttachment":"string","documentSpecification":{"fin":"string","swe":"string","smn":"string","sms":"string","sme":"string","eng":"string"},"documentCreatorOperators":[{"planOperatorKey":"string","planOperatorUri":"string","firstName":"string","lastName":"string","title":"string","organizationName":"string","businessId":"string"}],"relatedPlanAttachmentDocuments":["string"]}],"planThemes":["string"],"periodOfValidity":{"begin":"string","end":"string"},"recommendationNumber":0}],"colorNumber":"string","groupNumber":0}],"planRegulationGroupRelations":[{"planObjectKey":"string","planRegulationGroupKey":"string"}],"relatedPlanObjectRegulationGroupRelations":[{"relatedPlanObjectUri":"string","regulationGroupKey":"string"}]} # ValidatePlan | Yksittäinen kaava. (optional)

    try:
        # Rajapinta yksittäisen kaavan validointiin ilman kaava-asiaa.
        api_instance.post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin(plan_type, administrative_area_identifiers, validate_plan=validate_plan)
    except Exception as e:
        print("Exception when calling PlanApi->post_api_plan_validate_plantype_plantype_administrativeareaidentifiers_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_type** | **str**| Kaavalaji-koodiston arvo http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji | 
 **administrative_area_identifiers** | [**List[str]**](str.md)| Kunta- tai maakuntakoodi.     Esimerkki : 049 | 
 **validate_plan** | [**ValidatePlan**](ValidatePlan.md)| Yksittäinen kaava. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

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

