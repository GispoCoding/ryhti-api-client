from typing import Union

from ryhti_api_client.models.geo_json_line_string_geometry import (
    GeoJsonLineStringGeometry,
)
from ryhti_api_client.models.geo_json_multi_line_string_geometry import (
    GeoJsonMultiLineStringGeometry,
)
from ryhti_api_client.models.geo_json_multi_point_geometry import (
    GeoJsonMultiPointGeometry,
)
from ryhti_api_client.models.geo_json_multi_polygon_geometry import (
    GeoJsonMultiPolygonGeometry,
)
from ryhti_api_client.models.geo_json_point_geometry import GeoJsonPointGeometry
from ryhti_api_client.models.geo_json_polygon_geometry import GeoJsonPolygonGeometry

GeoJsonGeometry = Union[
    GeoJsonLineStringGeometry,
    GeoJsonMultiLineStringGeometry,
    GeoJsonMultiPointGeometry,
    GeoJsonMultiPolygonGeometry,
    GeoJsonPointGeometry,
    GeoJsonPolygonGeometry,
]

__all__ = ["GeoJsonGeometry"]
