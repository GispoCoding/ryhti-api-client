# CancelledGroupRelations

KumottavanRyhmänKohdistus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_regulation_group_uri** | **str** | Kaavamääräysryhmän kohdistamiseen käytettävä tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planregulationgroup/{planRegulationGroupKey}) | 
**plan_object_uri** | **str** | Kaavakohteen kohdistamiseen käytettävä tunnus URI-muodossa (https://uri.rakennetunymparistontietojarjestelma.fi/planobject/{planObjectKey}) | 

## Example

```python
from ryhti_api_client.models.cancelled_group_relations import CancelledGroupRelations

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledGroupRelations from a JSON string
cancelled_group_relations_instance = CancelledGroupRelations.from_json(json)
# print the JSON string representation of the object
print(CancelledGroupRelations.to_json())

# convert the object into a dict
cancelled_group_relations_dict = cancelled_group_relations_instance.to_dict()
# create an instance of CancelledGroupRelations from a dict
cancelled_group_relations_from_dict = CancelledGroupRelations.from_dict(cancelled_group_relations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


