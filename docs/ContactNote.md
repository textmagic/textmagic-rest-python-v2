# ContactNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contact note ID. | 
**created_at** | **datetime** | Contact note creation time. | 
**note** | **str** | Contact note text. | 
**user** | [**User**](User.md) |  | 

## Example

```python
from TextMagic.models.contact_note import ContactNote

# TODO update the JSON string below
json = "{}"
# create an instance of ContactNote from a JSON string
contact_note_instance = ContactNote.from_json(json)
# print the JSON string representation of the object
print(ContactNote.to_json())

# convert the object into a dict
contact_note_dict = contact_note_instance.to_dict()
# create an instance of ContactNote from a dict
contact_note_from_dict = ContactNote.from_dict(contact_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


