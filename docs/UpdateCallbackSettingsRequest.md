# UpdateCallbackSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_url** | **str** | This URL is used to push message delivery status updates to your application. | [optional] 
**in_url** | **str** | This URL is used to push incoming SMS to your application. | [optional] 
**format** | **str** | Desired callback data format. m - multipart/form-data, u - application/x-www-form-urlencoded, j - application/json | [optional] 

## Example

```python
from TextMagic.models.update_callback_settings_request import UpdateCallbackSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCallbackSettingsRequest from a JSON string
update_callback_settings_request_instance = UpdateCallbackSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCallbackSettingsRequest.to_json())

# convert the object into a dict
update_callback_settings_request_dict = update_callback_settings_request_instance.to_dict()
# create an instance of UpdateCallbackSettingsRequest from a dict
update_callback_settings_request_from_dict = UpdateCallbackSettingsRequest.from_dict(update_callback_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


