# GetSenderIdsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[SenderId]**](SenderId.md) |  | 

## Example

```python
from TextMagic.models.get_sender_ids_paginated_response import GetSenderIdsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderIdsPaginatedResponse from a JSON string
get_sender_ids_paginated_response_instance = GetSenderIdsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetSenderIdsPaginatedResponse.to_json())

# convert the object into a dict
get_sender_ids_paginated_response_dict = get_sender_ids_paginated_response_instance.to_dict()
# create an instance of GetSenderIdsPaginatedResponse from a dict
get_sender_ids_paginated_response_from_dict = GetSenderIdsPaginatedResponse.from_dict(get_sender_ids_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


