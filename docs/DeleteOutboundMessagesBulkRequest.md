# DeleteOutboundMessagesBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **int** | Default is 0 (false). If set to 1, all the entities will be removed. | [optional] 

## Example

```python
from TextMagic.models.delete_outbound_messages_bulk_request import DeleteOutboundMessagesBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOutboundMessagesBulkRequest from a JSON string
delete_outbound_messages_bulk_request_instance = DeleteOutboundMessagesBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOutboundMessagesBulkRequest.to_json())

# convert the object into a dict
delete_outbound_messages_bulk_request_dict = delete_outbound_messages_bulk_request_instance.to_dict()
# create an instance of DeleteOutboundMessagesBulkRequest from a dict
delete_outbound_messages_bulk_request_from_dict = DeleteOutboundMessagesBulkRequest.from_dict(delete_outbound_messages_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


