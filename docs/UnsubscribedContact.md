# UnsubscribedContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unsubscribed contact ID. | 
**phone** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | 
**unsubscribe_time** | **datetime** | Time when contact was opted-out. | 
**first_name** | **str** | Unsubscribed contact first name. | 
**last_name** | **str** | Unsubscribed contact last name. | 

## Example

```python
from TextMagic.models.unsubscribed_contact import UnsubscribedContact

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubscribedContact from a JSON string
unsubscribed_contact_instance = UnsubscribedContact.from_json(json)
# print the JSON string representation of the object
print(UnsubscribedContact.to_json())

# convert the object into a dict
unsubscribed_contact_dict = unsubscribed_contact_instance.to_dict()
# create an instance of UnsubscribedContact from a dict
unsubscribed_contact_from_dict = UnsubscribedContact.from_dict(unsubscribed_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


