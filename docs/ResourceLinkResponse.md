# ResourceLinkResponse

Response contains paginated list of data items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resource ID. | 
**href** | **str** | A link to this resource. If you want to fetch it, just **GET** this address. | 

## Example

```python
from TextMagic.models.resource_link_response import ResourceLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLinkResponse from a JSON string
resource_link_response_instance = ResourceLinkResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceLinkResponse.to_json())

# convert the object into a dict
resource_link_response_dict = resource_link_response_instance.to_dict()
# create an instance of ResourceLinkResponse from a dict
resource_link_response_from_dict = ResourceLinkResponse.from_dict(resource_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


