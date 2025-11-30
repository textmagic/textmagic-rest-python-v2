# MuteChatsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **bool** | Entity ID(s), separated by comma | [optional] 
**var_for** | **int** | Mute for N hours. | [optional] 

## Example

```python
from TextMagic.models.mute_chats_bulk_request import MuteChatsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MuteChatsBulkRequest from a JSON string
mute_chats_bulk_request_instance = MuteChatsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(MuteChatsBulkRequest.to_json())

# convert the object into a dict
mute_chats_bulk_request_dict = mute_chats_bulk_request_instance.to_dict()
# create an instance of MuteChatsBulkRequest from a dict
mute_chats_bulk_request_from_dict = MuteChatsBulkRequest.from_dict(mute_chats_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


