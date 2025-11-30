# DeleteScheduledMessagesBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **int** | Default is 0 (false). If set to 1, all the entities will be removed. | [optional] 
**status** | **str** | Default is an empty string (false). If set, all entities with specified status will be affected. | [optional] [default to '']

## Example

```python
from TextMagic.models.delete_scheduled_messages_bulk_request import DeleteScheduledMessagesBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScheduledMessagesBulkRequest from a JSON string
delete_scheduled_messages_bulk_request_instance = DeleteScheduledMessagesBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteScheduledMessagesBulkRequest.to_json())

# convert the object into a dict
delete_scheduled_messages_bulk_request_dict = delete_scheduled_messages_bulk_request_instance.to_dict()
# create an instance of DeleteScheduledMessagesBulkRequest from a dict
delete_scheduled_messages_bulk_request_from_dict = DeleteScheduledMessagesBulkRequest.from_dict(delete_scheduled_messages_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


