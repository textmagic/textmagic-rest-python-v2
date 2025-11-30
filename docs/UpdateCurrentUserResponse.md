# UpdateCurrentUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username. | [optional] 
**first_name** | **str** | Account first name. | [optional] 
**last_name** | **str** | Account last name. | [optional] 
**email** | **str** | User email address. | [optional] 
**phone** | **str** |  | [optional] 
**company** | **str** | Account company name. | [optional] 
**timezone** | **int** | Internal timezone ID. See [Get timezones](https://docs.textmagic.com/#operation/getTimezones). | [optional] 

## Example

```python
from TextMagic.models.update_current_user_response import UpdateCurrentUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCurrentUserResponse from a JSON string
update_current_user_response_instance = UpdateCurrentUserResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCurrentUserResponse.to_json())

# convert the object into a dict
update_current_user_response_dict = update_current_user_response_instance.to_dict()
# create an instance of UpdateCurrentUserResponse from a dict
update_current_user_response_from_dict = UpdateCurrentUserResponse.from_dict(update_current_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


