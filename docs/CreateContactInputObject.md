# CreateContactInputObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name. | [optional] 
**last_name** | **str** | Contact last name. | [optional] 
**phone** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | [optional] 
**email** | **str** | Contact email address. | [optional] 
**company_name** | **str** | Company name. | [optional] 
**lists** | **str** | Contact [list](https://docs.textmagic.com/#tag/Lists) ID. Each contact must be assigned to at least one list. | [optional] 
**favorited** | **bool** | Is the contact marked as favorite? | [optional] 
**blocked** | **bool** | Is the contact blocked for outgoing and incoming messaging? | [optional] 
**type** | **int** | Force type of phone. Possible values: 0 is landline; 1 is mobile; default is -1 (auto-detection). | [optional] 
**custom_field_values** | [**list[CustomFieldListItem]**](CustomFieldListItem.md) |  | [optional] 
**local** | **int** | Treat phone numbers passed in the request body as local. | [optional] 
**country** | **str** | The 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is the account country. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


