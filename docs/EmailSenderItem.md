# EmailSenderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique email sender identifier. | 
**domain_id** | **int** | ID of the associated domain. | 
**email** | **str** | Email address of the sender. | 
**created_at** | **datetime** | When the email sender was created. | 
**domain_status** | **str** | Current verification status of the associated domain. | 
**from_name** | **str** | Display name for the sender. | [optional] 
**reply_to** | **str** | Reply-to email address. | [optional] 

## Example

```python
from TextMagic.models.email_sender_item import EmailSenderItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSenderItem from a JSON string
email_sender_item_instance = EmailSenderItem.from_json(json)
# print the JSON string representation of the object
print(EmailSenderItem.to_json())

# convert the object into a dict
email_sender_item_dict = email_sender_item_instance.to_dict()
# create an instance of EmailSenderItem from a dict
email_sender_item_from_dict = EmailSenderItem.from_dict(email_sender_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


