# ClearAndAssignContactsToListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **str** | Contact ID(s), separated by a comma or \&quot;all\&quot; to add all contacts belonging to the current user. | [optional] 

## Example

```python
from TextMagic.models.clear_and_assign_contacts_to_list_request import ClearAndAssignContactsToListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearAndAssignContactsToListRequest from a JSON string
clear_and_assign_contacts_to_list_request_instance = ClearAndAssignContactsToListRequest.from_json(json)
# print the JSON string representation of the object
print(ClearAndAssignContactsToListRequest.to_json())

# convert the object into a dict
clear_and_assign_contacts_to_list_request_dict = clear_and_assign_contacts_to_list_request_instance.to_dict()
# create an instance of ClearAndAssignContactsToListRequest from a dict
clear_and_assign_contacts_to_list_request_from_dict = ClearAndAssignContactsToListRequest.from_dict(clear_and_assign_contacts_to_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


