# GetSurveysPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_count** | **int** | The total number of pages. | 
**limit** | **int** | The number of results per page. | 
**resources** | [**List[Survey]**](Survey.md) |  | 

## Example

```python
from TextMagic.models.get_surveys_paginated_response import GetSurveysPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSurveysPaginatedResponse from a JSON string
get_surveys_paginated_response_instance = GetSurveysPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetSurveysPaginatedResponse.to_json())

# convert the object into a dict
get_surveys_paginated_response_dict = get_surveys_paginated_response_instance.to_dict()
# create an instance of GetSurveysPaginatedResponse from a dict
get_surveys_paginated_response_from_dict = GetSurveysPaginatedResponse.from_dict(get_surveys_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


