# CreateContactNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Contact Note text. | [optional] 

## Example

```python
from TextMagic.models.create_contact_note_request import CreateContactNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactNoteRequest from a JSON string
create_contact_note_request_instance = CreateContactNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactNoteRequest.to_json())

# convert the object into a dict
create_contact_note_request_dict = create_contact_note_request_instance.to_dict()
# create an instance of CreateContactNoteRequest from a dict
create_contact_note_request_from_dict = CreateContactNoteRequest.from_dict(create_contact_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


