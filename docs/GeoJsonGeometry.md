# GeoJsonGeometry

`GeoJsonGeometry` is a `typing.Union` of the concrete models below. The variant is chosen by the `type` field (pydantic discriminated union).

type value | Model
------------ | -------------
`LineString` | [**GeoJsonLineStringGeometry**](GeoJsonLineStringGeometry.md)
`MultiLineString` | [**GeoJsonMultiLineStringGeometry**](GeoJsonMultiLineStringGeometry.md)
`MultiPoint` | [**GeoJsonMultiPointGeometry**](GeoJsonMultiPointGeometry.md)
`MultiPolygon` | [**GeoJsonMultiPolygonGeometry**](GeoJsonMultiPolygonGeometry.md)
`Point` | [**GeoJsonPointGeometry**](GeoJsonPointGeometry.md)
`Polygon` | [**GeoJsonPolygonGeometry**](GeoJsonPolygonGeometry.md)

## Example

```python
from ryhti_api_client.models.geo_json_line_string_geometry import GeoJsonLineStringGeometry
from ryhti_api_client.models.ryhti_geometry import RyhtiGeometry

obj = RyhtiGeometry.from_dict({..., "geometry": {"type": "LineString", ...}})
assert isinstance(obj.geometry, GeoJsonLineStringGeometry)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
