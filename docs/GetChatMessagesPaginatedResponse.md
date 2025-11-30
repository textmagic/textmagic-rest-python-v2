# GetChatMessagesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Conversation]**](Conversation.md) |  | 

## Example

```python
from TextMagic.models.get_chat_messages_paginated_response import GetChatMessagesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMessagesPaginatedResponse from a JSON string
get_chat_messages_paginated_response_instance = GetChatMessagesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatMessagesPaginatedResponse.to_json())

# convert the object into a dict
get_chat_messages_paginated_response_dict = get_chat_messages_paginated_response_instance.to_dict()
# create an instance of GetChatMessagesPaginatedResponse from a dict
get_chat_messages_paginated_response_from_dict = GetChatMessagesPaginatedResponse.from_dict(get_chat_messages_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


