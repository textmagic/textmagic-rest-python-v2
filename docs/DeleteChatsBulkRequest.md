# DeleteChatsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **bool** | Entity ID(s), separated by comma. | [optional] 
**status** | **str** | Default is an empty string. If set, all entities with specified status will be affected. | [optional] 

## Example

```python
from TextMagic.models.delete_chats_bulk_request import DeleteChatsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatsBulkRequest from a JSON string
delete_chats_bulk_request_instance = DeleteChatsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatsBulkRequest.to_json())

# convert the object into a dict
delete_chats_bulk_request_dict = delete_chats_bulk_request_instance.to_dict()
# create an instance of DeleteChatsBulkRequest from a dict
delete_chats_bulk_request_from_dict = DeleteChatsBulkRequest.from_dict(delete_chats_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


