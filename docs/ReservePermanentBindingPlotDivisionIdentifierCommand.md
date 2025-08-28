# ReservePermanentBindingPlotDivisionIdentifierCommand

Sanoma tonttijaon pysyvien tunnisteiden varaamiseen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area_identifier** | **str** | Hallinnollisen alueen tunnus (esim. kunta tai maakunta) | [optional] 
**project_name** | **str** | Kaavahankkeen pysyvä nimi. Nimi on uniikki eikä sitä voi vaihtaa. | [optional] 

## Example

```python
from ryhti_api_client.models.reserve_permanent_binding_plot_division_identifier_command import ReservePermanentBindingPlotDivisionIdentifierCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReservePermanentBindingPlotDivisionIdentifierCommand from a JSON string
reserve_permanent_binding_plot_division_identifier_command_instance = ReservePermanentBindingPlotDivisionIdentifierCommand.from_json(json)
# print the JSON string representation of the object
print(ReservePermanentBindingPlotDivisionIdentifierCommand.to_json())

# convert the object into a dict
reserve_permanent_binding_plot_division_identifier_command_dict = reserve_permanent_binding_plot_division_identifier_command_instance.to_dict()
# create an instance of ReservePermanentBindingPlotDivisionIdentifierCommand from a dict
reserve_permanent_binding_plot_division_identifier_command_from_dict = ReservePermanentBindingPlotDivisionIdentifierCommand.from_dict(reserve_permanent_binding_plot_division_identifier_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


