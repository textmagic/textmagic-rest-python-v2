# DeleteContactsByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Entity ID(s), separated by comma. | [optional] 
**all** | **int** | Optional. Default is 0 (false). If set to 1 all the entities will be removed. | [optional] 

## Example

```python
from TextMagic.models.delete_contacts_by_ids_request import DeleteContactsByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteContactsByIdsRequest from a JSON string
delete_contacts_by_ids_request_instance = DeleteContactsByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteContactsByIdsRequest.to_json())

# convert the object into a dict
delete_contacts_by_ids_request_dict = delete_contacts_by_ids_request_instance.to_dict()
# create an instance of DeleteContactsByIdsRequest from a dict
delete_contacts_by_ids_request_from_dict = DeleteContactsByIdsRequest.from_dict(delete_contacts_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


