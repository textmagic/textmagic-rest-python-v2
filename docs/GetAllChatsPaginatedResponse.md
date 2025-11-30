# GetAllChatsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Chat]**](Chat.md) |  | 

## Example

```python
from TextMagic.models.get_all_chats_paginated_response import GetAllChatsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllChatsPaginatedResponse from a JSON string
get_all_chats_paginated_response_instance = GetAllChatsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllChatsPaginatedResponse.to_json())

# convert the object into a dict
get_all_chats_paginated_response_dict = get_all_chats_paginated_response_instance.to_dict()
# create an instance of GetAllChatsPaginatedResponse from a dict
get_all_chats_paginated_response_from_dict = GetAllChatsPaginatedResponse.from_dict(get_all_chats_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


