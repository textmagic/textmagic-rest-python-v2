# GetAllBulkSessionsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[BulkSession]**](BulkSession.md) |  | 

## Example

```python
from TextMagic.models.get_all_bulk_sessions_paginated_response import GetAllBulkSessionsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllBulkSessionsPaginatedResponse from a JSON string
get_all_bulk_sessions_paginated_response_instance = GetAllBulkSessionsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllBulkSessionsPaginatedResponse.to_json())

# convert the object into a dict
get_all_bulk_sessions_paginated_response_dict = get_all_bulk_sessions_paginated_response_instance.to_dict()
# create an instance of GetAllBulkSessionsPaginatedResponse from a dict
get_all_bulk_sessions_paginated_response_from_dict = GetAllBulkSessionsPaginatedResponse.from_dict(get_all_bulk_sessions_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


