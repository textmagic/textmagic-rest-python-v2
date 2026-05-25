# GetListsOfContactPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[TmList]**](TmList.md) |  | 

## Example

```python
from TextMagic.models.get_lists_of_contact_paginated_response import GetListsOfContactPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetListsOfContactPaginatedResponse from a JSON string
get_lists_of_contact_paginated_response_instance = GetListsOfContactPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetListsOfContactPaginatedResponse.to_json())

# convert the object into a dict
get_lists_of_contact_paginated_response_dict = get_lists_of_contact_paginated_response_instance.to_dict()
# create an instance of GetListsOfContactPaginatedResponse from a dict
get_lists_of_contact_paginated_response_from_dict = GetListsOfContactPaginatedResponse.from_dict(get_lists_of_contact_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


