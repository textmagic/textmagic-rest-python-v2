# GetMessagePreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[MessageOut]**](MessageOut.md) |  | [optional] 

## Example

```python
from TextMagic.models.get_message_preview_response import GetMessagePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagePreviewResponse from a JSON string
get_message_preview_response_instance = GetMessagePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessagePreviewResponse.to_json())

# convert the object into a dict
get_message_preview_response_dict = get_message_preview_response_instance.to_dict()
# create an instance of GetMessagePreviewResponse from a dict
get_message_preview_response_from_dict = GetMessagePreviewResponse.from_dict(get_message_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


