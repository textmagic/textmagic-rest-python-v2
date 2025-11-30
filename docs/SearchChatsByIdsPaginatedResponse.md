# SearchChatsByIdsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Chat]**](Chat.md) |  | 

## Example

```python
from TextMagic.models.search_chats_by_ids_paginated_response import SearchChatsByIdsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchChatsByIdsPaginatedResponse from a JSON string
search_chats_by_ids_paginated_response_instance = SearchChatsByIdsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SearchChatsByIdsPaginatedResponse.to_json())

# convert the object into a dict
search_chats_by_ids_paginated_response_dict = search_chats_by_ids_paginated_response_instance.to_dict()
# create an instance of SearchChatsByIdsPaginatedResponse from a dict
search_chats_by_ids_paginated_response_from_dict = SearchChatsByIdsPaginatedResponse.from_dict(search_chats_by_ids_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


