# GetBlockedContactsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Contact]**](Contact.md) |  | 

## Example

```python
from TextMagic.models.get_blocked_contacts_paginated_response import GetBlockedContactsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockedContactsPaginatedResponse from a JSON string
get_blocked_contacts_paginated_response_instance = GetBlockedContactsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetBlockedContactsPaginatedResponse.to_json())

# convert the object into a dict
get_blocked_contacts_paginated_response_dict = get_blocked_contacts_paginated_response_instance.to_dict()
# create an instance of GetBlockedContactsPaginatedResponse from a dict
get_blocked_contacts_paginated_response_from_dict = GetBlockedContactsPaginatedResponse.from_dict(get_blocked_contacts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


