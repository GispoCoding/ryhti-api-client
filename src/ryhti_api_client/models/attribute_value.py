from typing import Union
from ryhti_api_client.models.code_value import CodeValue
from ryhti_api_client.models.decimal_range import DecimalRange
from ryhti_api_client.models.decimal_value import DecimalValue
from ryhti_api_client.models.identifier_value import IdentifierValue
from ryhti_api_client.models.localized_text_value import LocalizedTextValue
from ryhti_api_client.models.numeric_range import NumericRange
from ryhti_api_client.models.numeric_value import NumericValue
from ryhti_api_client.models.positive_decimal_range import PositiveDecimalRange
from ryhti_api_client.models.positive_decimal_value import PositiveDecimalValue
from ryhti_api_client.models.positive_numeric_range import PositiveNumericRange
from ryhti_api_client.models.positive_numeric_value import PositiveNumericValue
from ryhti_api_client.models.spot_elevation import SpotElevation
from ryhti_api_client.models.text_value import TextValue
from ryhti_api_client.models.time_period_date_only_value import TimePeriodDateOnlyValue
from ryhti_api_client.models.time_period_value import TimePeriodValue


AttributeValue = Union[
    CodeValue,
    DecimalRange,
    DecimalValue,
    IdentifierValue,
    LocalizedTextValue,
    NumericRange,
    NumericValue,
    PositiveDecimalRange,
    PositiveDecimalValue,
    PositiveNumericRange,
    PositiveNumericValue,
    SpotElevation,
    TextValue,
    TimePeriodDateOnlyValue,
    TimePeriodValue,
]

__all__ = ["AttributeValue"]