# GetContactsAutocompleteResponseItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Id of entity. 0 if object is a Reply | 
**entity_type** | **str** | Entry type: * **contact** if it is related to a contact * **list** if it is related to a contact list * **reply** if it is related to an incoming message  | 
**value** | **str** | Id of contact/list if entityType is contact/list OR phone number if entityType is reply. | 
**label** | **str** | Name of the contact/list if entityType is contact/list OR phone number if entityType is reply. | 
**shared_by** | **str** | If contact or list was shared by another sub-account then name if this user will be shown. | 
**avatar** | **str** | Contact avatar URI. | 
**favorited** | **bool** | If contact has been marked as favorite. | 
**user_id** | **int** | Owner id of the contact/list (if it was shared). | 
**country_name** | **str** |  | 
**qposition** | **int** |  | 
**rposition** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


