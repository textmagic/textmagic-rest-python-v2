# SetChatStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Chat ID. | [optional] 
**status** | **str** | Chat status:   * **a** - Active;   * **c** - Closed;   * **d** - Deleted.  | [optional] 

## Example

```python
from TextMagic.models.set_chat_status_request import SetChatStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatStatusRequest from a JSON string
set_chat_status_request_instance = SetChatStatusRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatStatusRequest.to_json())

# convert the object into a dict
set_chat_status_request_dict = set_chat_status_request_instance.to_dict()
# create an instance of SetChatStatusRequest from a dict
set_chat_status_request_from_dict = SetChatStatusRequest.from_dict(set_chat_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


