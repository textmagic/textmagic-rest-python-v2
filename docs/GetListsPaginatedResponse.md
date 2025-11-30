# GetListsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | **List[List]** |  | 

## Example

```python
from TextMagic.models.get_lists_paginated_response import GetListsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetListsPaginatedResponse from a JSON string
get_lists_paginated_response_instance = GetListsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetListsPaginatedResponse.to_json())

# convert the object into a dict
get_lists_paginated_response_dict = get_lists_paginated_response_instance.to_dict()
# create an instance of GetListsPaginatedResponse from a dict
get_lists_paginated_response_from_dict = GetListsPaginatedResponse.from_dict(get_lists_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


