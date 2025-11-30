# SearchContactsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Contact]**](Contact.md) |  | 

## Example

```python
from TextMagic.models.search_contacts_paginated_response import SearchContactsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchContactsPaginatedResponse from a JSON string
search_contacts_paginated_response_instance = SearchContactsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SearchContactsPaginatedResponse.to_json())

# convert the object into a dict
search_contacts_paginated_response_dict = search_contacts_paginated_response_instance.to_dict()
# create an instance of SearchContactsPaginatedResponse from a dict
search_contacts_paginated_response_from_dict = SearchContactsPaginatedResponse.from_dict(search_contacts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


