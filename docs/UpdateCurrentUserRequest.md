# UpdateCurrentUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**first_name** | **str** | Account first name. | [optional] 
**last_name** | **str** | Account last name. | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**company** | **str** | Account company name. | [optional] 
**timezone** | **int** | The timezome internal ID. See [Get timezones](https://docs.textmagic.com/#operation/getTimezones). | [optional] 

## Example

```python
from TextMagic.models.update_current_user_request import UpdateCurrentUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCurrentUserRequest from a JSON string
update_current_user_request_instance = UpdateCurrentUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCurrentUserRequest.to_json())

# convert the object into a dict
update_current_user_request_dict = update_current_user_request_instance.to_dict()
# create an instance of UpdateCurrentUserRequest from a dict
update_current_user_request_from_dict = UpdateCurrentUserRequest.from_dict(update_current_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


