# GetCustomFieldsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[UserCustomField]**](UserCustomField.md) |  | 

## Example

```python
from TextMagic.models.get_custom_fields_paginated_response import GetCustomFieldsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomFieldsPaginatedResponse from a JSON string
get_custom_fields_paginated_response_instance = GetCustomFieldsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomFieldsPaginatedResponse.to_json())

# convert the object into a dict
get_custom_fields_paginated_response_dict = get_custom_fields_paginated_response_instance.to_dict()
# create an instance of GetCustomFieldsPaginatedResponse from a dict
get_custom_fields_paginated_response_from_dict = GetCustomFieldsPaginatedResponse.from_dict(get_custom_fields_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


