# ParticipationAndAssessmentScheme

OsallistumisJaArviointiSuunnitelma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participation_and_assessment_scheme_key** | **str** | Tiedon tuottajatahon tietojärjestelmän generoima kohteen versioriippumaton tunnus | 
**participation_and_assessment_scheme_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/participationandassessmentscheme/{guid}) | [optional] [readonly] 
**attachment_documents** | [**List[PlanAttachmentDocument]**](PlanAttachmentDocument.md) |  | 

## Example

```python
from ryhti_api_client.models.participation_and_assessment_scheme import ParticipationAndAssessmentScheme

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipationAndAssessmentScheme from a JSON string
participation_and_assessment_scheme_instance = ParticipationAndAssessmentScheme.from_json(json)
# print the JSON string representation of the object
print(ParticipationAndAssessmentScheme.to_json())

# convert the object into a dict
participation_and_assessment_scheme_dict = participation_and_assessment_scheme_instance.to_dict()
# create an instance of ParticipationAndAssessmentScheme from a dict
participation_and_assessment_scheme_from_dict = ParticipationAndAssessmentScheme.from_dict(participation_and_assessment_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


