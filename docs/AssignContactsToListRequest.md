# AssignContactsToListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **str** | Comma-separated array of [Contacts](https://docs.textmagic.com/#tag/Contacts) IDs. | [optional] 

## Example

```python
from TextMagic.models.assign_contacts_to_list_request import AssignContactsToListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignContactsToListRequest from a JSON string
assign_contacts_to_list_request_instance = AssignContactsToListRequest.from_json(json)
# print the JSON string representation of the object
print(AssignContactsToListRequest.to_json())

# convert the object into a dict
assign_contacts_to_list_request_dict = assign_contacts_to_list_request_instance.to_dict()
# create an instance of AssignContactsToListRequest from a dict
assign_contacts_to_list_request_from_dict = AssignContactsToListRequest.from_dict(assign_contacts_to_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


