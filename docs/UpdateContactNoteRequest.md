# UpdateContactNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Contact Note text. | [optional] 

## Example

```python
from TextMagic.models.update_contact_note_request import UpdateContactNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactNoteRequest from a JSON string
update_contact_note_request_instance = UpdateContactNoteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactNoteRequest.to_json())

# convert the object into a dict
update_contact_note_request_dict = update_contact_note_request_instance.to_dict()
# create an instance of UpdateContactNoteRequest from a dict
update_contact_note_request_from_dict = UpdateContactNoteRequest.from_dict(update_contact_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


