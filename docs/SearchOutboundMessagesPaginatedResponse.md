# SearchOutboundMessagesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[MessageOut]**](MessageOut.md) |  | 

## Example

```python
from TextMagic.models.search_outbound_messages_paginated_response import SearchOutboundMessagesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOutboundMessagesPaginatedResponse from a JSON string
search_outbound_messages_paginated_response_instance = SearchOutboundMessagesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SearchOutboundMessagesPaginatedResponse.to_json())

# convert the object into a dict
search_outbound_messages_paginated_response_dict = search_outbound_messages_paginated_response_instance.to_dict()
# create an instance of SearchOutboundMessagesPaginatedResponse from a dict
search_outbound_messages_paginated_response_from_dict = SearchOutboundMessagesPaginatedResponse.from_dict(search_outbound_messages_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


