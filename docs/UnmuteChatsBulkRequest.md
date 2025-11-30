# UnmuteChatsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **bool** | Entity ID(s), separated by comma | [optional] 

## Example

```python
from TextMagic.models.unmute_chats_bulk_request import UnmuteChatsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnmuteChatsBulkRequest from a JSON string
unmute_chats_bulk_request_instance = UnmuteChatsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(UnmuteChatsBulkRequest.to_json())

# convert the object into a dict
unmute_chats_bulk_request_dict = unmute_chats_bulk_request_instance.to_dict()
# create an instance of UnmuteChatsBulkRequest from a dict
unmute_chats_bulk_request_from_dict = UnmuteChatsBulkRequest.from_dict(unmute_chats_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


