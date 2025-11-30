# DoAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**token** | **str** |  | 
**expires** | **datetime** |  | 
**min_versions** | [**DoAuthResponseMinVersions**](DoAuthResponseMinVersions.md) |  | 
**disallowed_rules** | **List[str]** |  | 

## Example

```python
from TextMagic.models.do_auth_response import DoAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DoAuthResponse from a JSON string
do_auth_response_instance = DoAuthResponse.from_json(json)
# print the JSON string representation of the object
print(DoAuthResponse.to_json())

# convert the object into a dict
do_auth_response_dict = do_auth_response_instance.to_dict()
# create an instance of DoAuthResponse from a dict
do_auth_response_from_dict = DoAuthResponse.from_dict(do_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


