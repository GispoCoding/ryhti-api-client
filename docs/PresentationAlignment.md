# PresentationAlignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_object_key** | **UUID** | Key of the plan object this presentation alignment is associated with. | 
**plan_regulation_group_key** | **UUID** | Key of the plan regulation group this presentation alignment is associated with. | 
**geometry** | [**RyhtiGeometry**](RyhtiGeometry.md) | Geometry of the presentation alignment. Allowed types: Point, LineString. | 
**rotation** | **int** | Rotation of the presentation alignment in degrees. Allowed range: -360 to 360. | [optional] 
**language** | **str** | Language of the presentation alignment.  Code value from: http://uri.suomi.fi/codelist/rytj/ryhtikielet    Allowed values:  &lt;list type&#x3D;\&quot;bullet\&quot;&gt;&lt;item&gt;&lt;description&gt;fi - suomi&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;description&gt;sv - ruotsi&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;description&gt;en - englanti&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;description&gt;smn - inarinsaame&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;description&gt;sms - koltansaame&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;description&gt;se - pohjoissaame&lt;/description&gt;&lt;/item&gt;&lt;/list&gt; | [optional] 

## Example

```python
from ryhti_api_client.models.presentation_alignment import PresentationAlignment

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationAlignment from a JSON string
presentation_alignment_instance = PresentationAlignment.from_json(json)
# print the JSON string representation of the object
print(PresentationAlignment.to_json())

# convert the object into a dict
presentation_alignment_dict = presentation_alignment_instance.to_dict()
# create an instance of PresentationAlignment from a dict
presentation_alignment_from_dict = PresentationAlignment.from_dict(presentation_alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


