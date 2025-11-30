# GetCallbackSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_url** | **str** | This URL is used to push message delivery status updates to your application. | 
**in_url** | **str** | This URL is used to push incoming SMS to your application. | 
**format** | **str** | Desired callback data format. m - multipart/form-data, u - application/x-www-form-urlencoded, j - application/json. | 

## Example

```python
from TextMagic.models.get_callback_settings_response import GetCallbackSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCallbackSettingsResponse from a JSON string
get_callback_settings_response_instance = GetCallbackSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCallbackSettingsResponse.to_json())

# convert the object into a dict
get_callback_settings_response_dict = get_callback_settings_response_instance.to_dict()
# create an instance of GetCallbackSettingsResponse from a dict
get_callback_settings_response_from_dict = GetCallbackSettingsResponse.from_dict(get_callback_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


