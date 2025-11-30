# MarkChatsUnreadBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **bool** | Entity ID(s), separated by comma. | [optional] 

## Example

```python
from TextMagic.models.mark_chats_unread_bulk_request import MarkChatsUnreadBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkChatsUnreadBulkRequest from a JSON string
mark_chats_unread_bulk_request_instance = MarkChatsUnreadBulkRequest.from_json(json)
# print the JSON string representation of the object
print(MarkChatsUnreadBulkRequest.to_json())

# convert the object into a dict
mark_chats_unread_bulk_request_dict = mark_chats_unread_bulk_request_instance.to_dict()
# create an instance of MarkChatsUnreadBulkRequest from a dict
mark_chats_unread_bulk_request_from_dict = MarkChatsUnreadBulkRequest.from_dict(mark_chats_unread_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


