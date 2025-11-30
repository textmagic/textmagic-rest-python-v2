# UnblockContactsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **int** | Default is 0 (false). If set to 1, all entities will be removed. | [optional] 

## Example

```python
from TextMagic.models.unblock_contacts_bulk_request import UnblockContactsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnblockContactsBulkRequest from a JSON string
unblock_contacts_bulk_request_instance = UnblockContactsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(UnblockContactsBulkRequest.to_json())

# convert the object into a dict
unblock_contacts_bulk_request_dict = unblock_contacts_bulk_request_instance.to_dict()
# create an instance of UnblockContactsBulkRequest from a dict
unblock_contacts_bulk_request_from_dict = UnblockContactsBulkRequest.from_dict(unblock_contacts_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


