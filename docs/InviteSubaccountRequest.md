# InviteSubaccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The invitation email will be sent to this email address. | [optional] 
**role** | **str** | Type of account: *   **A** for Administrator sub-account; *   **U** for Regular User.  | [optional] 

## Example

```python
from TextMagic.models.invite_subaccount_request import InviteSubaccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteSubaccountRequest from a JSON string
invite_subaccount_request_instance = InviteSubaccountRequest.from_json(json)
# print the JSON string representation of the object
print(InviteSubaccountRequest.to_json())

# convert the object into a dict
invite_subaccount_request_dict = invite_subaccount_request_instance.to_dict()
# create an instance of InviteSubaccountRequest from a dict
invite_subaccount_request_from_dict = InviteSubaccountRequest.from_dict(invite_subaccount_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


