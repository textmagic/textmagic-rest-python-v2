# GetContactsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Contact]**](Contact.md) |  | 

## Example

```python
from TextMagic.models.get_contacts_paginated_response import GetContactsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactsPaginatedResponse from a JSON string
get_contacts_paginated_response_instance = GetContactsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetContactsPaginatedResponse.to_json())

# convert the object into a dict
get_contacts_paginated_response_dict = get_contacts_paginated_response_instance.to_dict()
# create an instance of GetContactsPaginatedResponse from a dict
get_contacts_paginated_response_from_dict = GetContactsPaginatedResponse.from_dict(get_contacts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


