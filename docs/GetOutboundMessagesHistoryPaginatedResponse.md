# GetOutboundMessagesHistoryPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_id** | **int** |  | 
**next_last_id** | **int** |  | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[MessageOut]**](MessageOut.md) |  | 

## Example

```python
from TextMagic.models.get_outbound_messages_history_paginated_response import GetOutboundMessagesHistoryPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOutboundMessagesHistoryPaginatedResponse from a JSON string
get_outbound_messages_history_paginated_response_instance = GetOutboundMessagesHistoryPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetOutboundMessagesHistoryPaginatedResponse.to_json())

# convert the object into a dict
get_outbound_messages_history_paginated_response_dict = get_outbound_messages_history_paginated_response_instance.to_dict()
# create an instance of GetOutboundMessagesHistoryPaginatedResponse from a dict
get_outbound_messages_history_paginated_response_from_dict = GetOutboundMessagesHistoryPaginatedResponse.from_dict(get_outbound_messages_history_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


