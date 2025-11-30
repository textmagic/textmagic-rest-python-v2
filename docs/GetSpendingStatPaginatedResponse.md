# GetSpendingStatPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[UserStatement]**](UserStatement.md) |  | 

## Example

```python
from TextMagic.models.get_spending_stat_paginated_response import GetSpendingStatPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpendingStatPaginatedResponse from a JSON string
get_spending_stat_paginated_response_instance = GetSpendingStatPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetSpendingStatPaginatedResponse.to_json())

# convert the object into a dict
get_spending_stat_paginated_response_dict = get_spending_stat_paginated_response_instance.to_dict()
# create an instance of GetSpendingStatPaginatedResponse from a dict
get_spending_stat_paginated_response_from_dict = GetSpendingStatPaginatedResponse.from_dict(get_spending_stat_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


