# GetAllInboundMessagesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[MessageIn]**](MessageIn.md) |  | 

## Example

```python
from TextMagic.models.get_all_inbound_messages_paginated_response import GetAllInboundMessagesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllInboundMessagesPaginatedResponse from a JSON string
get_all_inbound_messages_paginated_response_instance = GetAllInboundMessagesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllInboundMessagesPaginatedResponse.to_json())

# convert the object into a dict
get_all_inbound_messages_paginated_response_dict = get_all_inbound_messages_paginated_response_instance.to_dict()
# create an instance of GetAllInboundMessagesPaginatedResponse from a dict
get_all_inbound_messages_paginated_response_from_dict = GetAllInboundMessagesPaginatedResponse.from_dict(get_all_inbound_messages_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


