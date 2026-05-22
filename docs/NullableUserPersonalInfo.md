# NullableUserPersonalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID. | [optional] 
**first_name** | **str** | User&#39;s first name. | [optional] 
**last_name** | **str** | User&#39;s last name. | [optional] 
**avatar_url** | **str** | URL to user&#39;s avatar image. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 

## Example

```python
from TextMagic.models.nullable_user_personal_info import NullableUserPersonalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NullableUserPersonalInfo from a JSON string
nullable_user_personal_info_instance = NullableUserPersonalInfo.from_json(json)
# print the JSON string representation of the object
print(NullableUserPersonalInfo.to_json())

# convert the object into a dict
nullable_user_personal_info_dict = nullable_user_personal_info_instance.to_dict()
# create an instance of NullableUserPersonalInfo from a dict
nullable_user_personal_info_from_dict = NullableUserPersonalInfo.from_dict(nullable_user_personal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


