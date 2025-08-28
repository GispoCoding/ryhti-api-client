# BindingPlotDivisionCancellationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_binding_plot_division_uri** | **str** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/bindingplotdivision/{bindingplotdivisionkey}) kumoutuvaan sitovaan tonttijakoon. | 
**cancels_entire_binding_plot_division** | **bool** | Kumoaa sitovan tonttijaon kokonaan | 
**cancelled_plot_division_plot_uris** | **List[str]** | Viittaustunnus (https://uri.rakennetunymparistontietojarjestelma.fi/plotdivisionplot/{plotdivisionplotkey}) kumoutuviin tonttijakotontteihin. | [optional] 

## Example

```python
from ryhti_api_client.models.binding_plot_division_cancellation_info import BindingPlotDivisionCancellationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BindingPlotDivisionCancellationInfo from a JSON string
binding_plot_division_cancellation_info_instance = BindingPlotDivisionCancellationInfo.from_json(json)
# print the JSON string representation of the object
print(BindingPlotDivisionCancellationInfo.to_json())

# convert the object into a dict
binding_plot_division_cancellation_info_dict = binding_plot_division_cancellation_info_instance.to_dict()
# create an instance of BindingPlotDivisionCancellationInfo from a dict
binding_plot_division_cancellation_info_from_dict = BindingPlotDivisionCancellationInfo.from_dict(binding_plot_division_cancellation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


