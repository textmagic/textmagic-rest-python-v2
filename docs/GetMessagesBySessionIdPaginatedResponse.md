# GetMessagesBySessionIdPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[MessageOut]**](MessageOut.md) |  | 

## Example

```python
from TextMagic.models.get_messages_by_session_id_paginated_response import GetMessagesBySessionIdPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagesBySessionIdPaginatedResponse from a JSON string
get_messages_by_session_id_paginated_response_instance = GetMessagesBySessionIdPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessagesBySessionIdPaginatedResponse.to_json())

# convert the object into a dict
get_messages_by_session_id_paginated_response_dict = get_messages_by_session_id_paginated_response_instance.to_dict()
# create an instance of GetMessagesBySessionIdPaginatedResponse from a dict
get_messages_by_session_id_paginated_response_from_dict = GetMessagesBySessionIdPaginatedResponse.from_dict(get_messages_by_session_id_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


