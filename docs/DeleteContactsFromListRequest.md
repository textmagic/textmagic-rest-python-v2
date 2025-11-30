# DeleteContactsFromListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **str** | Comma-separated array of [Contacts](https://docs.textmagic.com/#tag/Contacts) IDs.  | [optional] 

## Example

```python
from TextMagic.models.delete_contacts_from_list_request import DeleteContactsFromListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteContactsFromListRequest from a JSON string
delete_contacts_from_list_request_instance = DeleteContactsFromListRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteContactsFromListRequest.to_json())

# convert the object into a dict
delete_contacts_from_list_request_dict = delete_contacts_from_list_request_instance.to_dict()
# create an instance of DeleteContactsFromListRequest from a dict
delete_contacts_from_list_request_from_dict = DeleteContactsFromListRequest.from_dict(delete_contacts_from_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


