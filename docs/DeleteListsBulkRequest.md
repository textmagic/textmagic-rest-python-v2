# DeleteListsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **int** | Default is 0 (false). If set to 1, all the entities will be removed. | [optional] 

## Example

```python
from TextMagic.models.delete_lists_bulk_request import DeleteListsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteListsBulkRequest from a JSON string
delete_lists_bulk_request_instance = DeleteListsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteListsBulkRequest.to_json())

# convert the object into a dict
delete_lists_bulk_request_dict = delete_lists_bulk_request_instance.to_dict()
# create an instance of DeleteListsBulkRequest from a dict
delete_lists_bulk_request_from_dict = DeleteListsBulkRequest.from_dict(delete_lists_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


