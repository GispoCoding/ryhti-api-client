# ValidatePlan

Kaava

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_key** | **UUID** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**plan_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/plan/{guid}) | [optional] [readonly] 
**life_cycle_status** | **str** | Kaavan elinkaaren tila. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari\&quot;&gt;http://uri.suomi.fi/codelist/rytj/kaavaelinkaari&lt;/a&gt; | 
**legal_effect_of_local_master_plans** | **List[str]** | Yleiskaavan oikeusvaikutteisuuden määritykset. Käytössä ainoastaan yleiskaavan yhteydessä. Käytetään koodistoa &lt;a href&#x3D;\&quot;http://uri.suomi.fi/codelist/rytj/oikeusvaik_YK\&quot;&gt;http://uri.suomi.fi/codelist/rytj/oikeusvaik_YK&lt;/a&gt; | [optional] 
**scale** | **int** | Mittakaava | [optional] 
**official_use_only** | **bool** | Vain viranomaiskäyttöön | [optional] 
**plan_maps** | [**List[PlanMap]**](PlanMap.md) | Kaavakartat | [optional] 
**geographical_area** | [**RyhtiGeometry**](RyhtiGeometry.md) | Aluerajaus | 
**plan_description** | **str** | Kaavan kuvaus | [optional] 
**plan_annexes** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) | Kaavan liittet | [optional] 
**other_plan_materials** | [**List[OtherPlanMaterial]**](OtherPlanMaterial.md) | Muu kaava-aineisto | [optional] 
**plan_cancellation_infos** | [**List[PlanCancellationInfo]**](PlanCancellationInfo.md) | Kumoamistieto | [optional] 
**plan_report** | [**PlanReport**](PlanReport.md) | Kaavaselostus | [optional] 
**general_regulation_groups** | [**List[GeneralRegulationGroup]**](GeneralRegulationGroup.md) | Kaavamääräysryhmät | [optional] 
**presentation_alignments** | [**List[PresentationAlignment]**](PresentationAlignment.md) | Esitystavankohdistus | [optional] 
**period_of_validity** | [**TimePeriodDateOnly**](TimePeriodDateOnly.md) | Voimassaoloaika | [optional] 
**approval_date** | **date** | Hyväksymispäivämäärä | [optional] 
**planners** | [**List[PlanOperator]**](PlanOperator.md) | Laatija | [optional] 
**plan_objects** | [**List[PlanObject]**](PlanObject.md) | Kaavakohteet | 
**plan_regulation_groups** | [**List[PlanRegulationGroup]**](PlanRegulationGroup.md) | Kaavakohteen määräysryhmät | 
**plan_regulation_group_relations** | [**List[PlanRegulationGroupRelations]**](PlanRegulationGroupRelations.md) | Kaavakohteen ja määräysryhmän väliset suhteet | [optional] 
**related_plan_object_regulation_group_relations** | [**List[RelatedPlanObjectRegulationGroupRelation]**](RelatedPlanObjectRegulationGroupRelation.md) |  | [optional] 

## Example

```python
from ryhti_api_client.models.validate_plan import ValidatePlan

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePlan from a JSON string
validate_plan_instance = ValidatePlan.from_json(json)
# print the JSON string representation of the object
print(ValidatePlan.to_json())

# convert the object into a dict
validate_plan_dict = validate_plan_instance.to_dict()
# create an instance of ValidatePlan from a dict
validate_plan_from_dict = ValidatePlan.from_dict(validate_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


