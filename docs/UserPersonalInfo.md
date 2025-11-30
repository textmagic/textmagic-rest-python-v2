# UserPersonalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID. | 
**first_name** | **str** | User&#39;s first name. | [optional] 
**last_name** | **str** | User&#39;s last name. | [optional] 
**avatar_url** | **str** | URL to user&#39;s avatar image. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 

## Example

```python
from TextMagic.models.user_personal_info import UserPersonalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalInfo from a JSON string
user_personal_info_instance = UserPersonalInfo.from_json(json)
# print the JSON string representation of the object
print(UserPersonalInfo.to_json())

# convert the object into a dict
user_personal_info_dict = user_personal_info_instance.to_dict()
# create an instance of UserPersonalInfo from a dict
user_personal_info_from_dict = UserPersonalInfo.from_dict(user_personal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


