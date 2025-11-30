# UpdateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name. | [optional] 
**last_name** | **str** | Contact last name. | [optional] 
**phone** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | [optional] 
**email** | **str** | Contact email address. | [optional] 
**company_name** | **str** | Contact company name. | [optional] 
**lists** | **str** | Comma-separated [list](https://docs.textmagic.com/#section/Lists) ID. Each contact must be assigned to at least one list. | [optional] 
**favorited** | **bool** | Is the contact marked as favorite? | [optional] 
**blocked** | **bool** | Is the contact blocked for outgoing and incoming messaging? | [optional] 
**type** | **int** | Force type of phone. Possible values: 0 is landline; 1 is mobile; default is -1 (auto-detection). | [optional] 
**custom_field_values** | [**List[CustomFieldListItem]**](CustomFieldListItem.md) |  | [optional] 
**local** | **int** | Treat phone numbers passed in the request body as **local**. | [optional] 
**country** | **str** | The 2-letter ISO country code for local phone numbers, used when **local** is set to true. | [optional] 
**tags** | **List[int]** | An array of tag IDs that will be assigned to the contact. | [optional] 
**owner** | **int** | Contact Owner ID | [optional] 

## Example

```python
from TextMagic.models.update_contact_request import UpdateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactRequest from a JSON string
update_contact_request_instance = UpdateContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactRequest.to_json())

# convert the object into a dict
update_contact_request_dict = update_contact_request_instance.to_dict()
# create an instance of UpdateContactRequest from a dict
update_contact_request_from_dict = UpdateContactRequest.from_dict(update_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


