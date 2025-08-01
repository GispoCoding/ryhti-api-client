# BindingPlotDivisionOperator

Toimija

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_plot_division_operator_key** | **str** | Toimijan avain | 
**binding_plot_division_operator_uri** | **str** | Luokan pysyvä URI -muotoinen viittaustunniste (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivisionoperator/{guid}) | [optional] [readonly] 
**first_name** | **str** | Etunimi | [optional] 
**last_name** | **str** | Sukunimi | [optional] 
**title** | **str** | Nimike | [optional] 
**organization_name** | **str** | Organisaation nimi | [optional] 
**business_id** | **str** | Y-tunnus | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division_operator import BindingPlotDivisionOperator

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivisionOperator from a JSON string
binding_plot_division_operator_instance = BindingPlotDivisionOperator.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivisionOperator.to_json())

# convert the object into a dict
binding_plot_division_operator_dict = binding_plot_division_operator_instance.to_dict()
# create an instance of BindingPlotDivisionOperator from a dict
binding_plot_division_operator_from_dict = BindingPlotDivisionOperator.from_dict(binding_plot_division_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


