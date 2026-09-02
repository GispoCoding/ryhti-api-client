# AttributeValue

`AttributeValue` is a `typing.Union` of the concrete models below. The variant is chosen by the `dataType` field (pydantic discriminated union).

dataType value | Model
------------ | -------------
`Code` | [**CodeValue**](CodeValue.md)
`Decimal` | [**DecimalValue**](DecimalValue.md)
`DecimalRange` | [**DecimalRange**](DecimalRange.md)
`Identifier` | [**IdentifierValue**](IdentifierValue.md)
`LocalizedText` | [**LocalizedTextValue**](LocalizedTextValue.md)
`Numeric` | [**NumericValue**](NumericValue.md)
`NumericRange` | [**NumericRange**](NumericRange.md)
`PositiveDecimal` | [**PositiveDecimalValue**](PositiveDecimalValue.md)
`PositiveDecimalRange` | [**PositiveDecimalRange**](PositiveDecimalRange.md)
`PositiveNumeric` | [**PositiveNumericValue**](PositiveNumericValue.md)
`PositiveNumericRange` | [**PositiveNumericRange**](PositiveNumericRange.md)
`SpotElevation` | [**SpotElevation**](SpotElevation.md)
`Text` | [**TextValue**](TextValue.md)
`TimePeriod` | [**TimePeriodValue**](TimePeriodValue.md)
`TimePeriodDateOnly` | [**TimePeriodDateOnlyValue**](TimePeriodDateOnlyValue.md)

## Example

```python
from ryhti_api_client.models.code_value import CodeValue
from ryhti_api_client.models.additional_information import AdditionalInformation

obj = AdditionalInformation.from_dict({..., "value": {"dataType": "Code", ...}})
assert isinstance(obj.value, CodeValue)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
