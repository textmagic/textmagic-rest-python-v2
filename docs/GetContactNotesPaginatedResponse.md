# GetContactNotesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[ContactNote]**](ContactNote.md) |  | 

## Example

```python
from TextMagic.models.get_contact_notes_paginated_response import GetContactNotesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactNotesPaginatedResponse from a JSON string
get_contact_notes_paginated_response_instance = GetContactNotesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetContactNotesPaginatedResponse.to_json())

# convert the object into a dict
get_contact_notes_paginated_response_dict = get_contact_notes_paginated_response_instance.to_dict()
# create an instance of GetContactNotesPaginatedResponse from a dict
get_contact_notes_paginated_response_from_dict = GetContactNotesPaginatedResponse.from_dict(get_contact_notes_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


