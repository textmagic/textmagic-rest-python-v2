# SearchScheduledMessagesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[MessagesIcs]**](MessagesIcs.md) |  | 

## Example

```python
from TextMagic.models.search_scheduled_messages_paginated_response import SearchScheduledMessagesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchScheduledMessagesPaginatedResponse from a JSON string
search_scheduled_messages_paginated_response_instance = SearchScheduledMessagesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SearchScheduledMessagesPaginatedResponse.to_json())

# convert the object into a dict
search_scheduled_messages_paginated_response_dict = search_scheduled_messages_paginated_response_instance.to_dict()
# create an instance of SearchScheduledMessagesPaginatedResponse from a dict
search_scheduled_messages_paginated_response_from_dict = SearchScheduledMessagesPaginatedResponse.from_dict(search_scheduled_messages_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


