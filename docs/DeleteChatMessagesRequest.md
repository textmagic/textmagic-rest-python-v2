# DeleteChatMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_ids** | **str** | Inbound message IDs to delete. Require when \&quot;all\&quot; is equal to 0 (false). | [optional] 
**sent_ids** | **str** | Sent message IDs to delete. Require when \&quot;all\&quot; is equal to 0 (false). | [optional] 
**calls_ids** | **str** | Calls IDs to delete. Require when \&quot;all\&quot; is equal to 0 (false). | [optional] 
**all** | **bool** | Default is 0 (false). If set to 1, all the entities will be removed. | [optional] 

## Example

```python
from TextMagic.models.delete_chat_messages_request import DeleteChatMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatMessagesRequest from a JSON string
delete_chat_messages_request_instance = DeleteChatMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatMessagesRequest.to_json())

# convert the object into a dict
delete_chat_messages_request_dict = delete_chat_messages_request_instance.to_dict()
# create an instance of DeleteChatMessagesRequest from a dict
delete_chat_messages_request_from_dict = DeleteChatMessagesRequest.from_dict(delete_chat_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


