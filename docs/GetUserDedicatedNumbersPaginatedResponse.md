# GetUserDedicatedNumbersPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[UsersInbound]**](UsersInbound.md) |  | 

## Example

```python
from TextMagic.models.get_user_dedicated_numbers_paginated_response import GetUserDedicatedNumbersPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserDedicatedNumbersPaginatedResponse from a JSON string
get_user_dedicated_numbers_paginated_response_instance = GetUserDedicatedNumbersPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserDedicatedNumbersPaginatedResponse.to_json())

# convert the object into a dict
get_user_dedicated_numbers_paginated_response_dict = get_user_dedicated_numbers_paginated_response_instance.to_dict()
# create an instance of GetUserDedicatedNumbersPaginatedResponse from a dict
get_user_dedicated_numbers_paginated_response_from_dict = GetUserDedicatedNumbersPaginatedResponse.from_dict(get_user_dedicated_numbers_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


