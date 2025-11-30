# DeleteContactNotesBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **bool** | Entity ID(s), separated by comma. | [optional] 

## Example

```python
from TextMagic.models.delete_contact_notes_bulk_request import DeleteContactNotesBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteContactNotesBulkRequest from a JSON string
delete_contact_notes_bulk_request_instance = DeleteContactNotesBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteContactNotesBulkRequest.to_json())

# convert the object into a dict
delete_contact_notes_bulk_request_dict = delete_contact_notes_bulk_request_instance.to_dict()
# create an instance of DeleteContactNotesBulkRequest from a dict
delete_contact_notes_bulk_request_from_dict = DeleteContactNotesBulkRequest.from_dict(delete_contact_notes_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


