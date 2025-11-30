# GetVersionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ios** | **str** |  | 
**android** | **str** |  | 
**desktop** | **str** |  | 

## Example

```python
from TextMagic.models.get_versions_response import GetVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVersionsResponse from a JSON string
get_versions_response_instance = GetVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetVersionsResponse.to_json())

# convert the object into a dict
get_versions_response_dict = get_versions_response_instance.to_dict()
# create an instance of GetVersionsResponse from a dict
get_versions_response_from_dict = GetVersionsResponse.from_dict(get_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


