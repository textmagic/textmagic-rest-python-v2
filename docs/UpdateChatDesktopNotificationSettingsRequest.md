# UpdateChatDesktopNotificationSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_sound** | **bool** | Enable notification sound? | [optional] 
**show_notifications** | **bool** | Show desktop notifications about new messages. | [optional] 
**show_text** | **bool** | Incoming message text will be displayed in desktop notifications. | [optional] 
**sound_id** | **int** | Sound Id of a notification. | [optional] 

## Example

```python
from TextMagic.models.update_chat_desktop_notification_settings_request import UpdateChatDesktopNotificationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatDesktopNotificationSettingsRequest from a JSON string
update_chat_desktop_notification_settings_request_instance = UpdateChatDesktopNotificationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateChatDesktopNotificationSettingsRequest.to_json())

# convert the object into a dict
update_chat_desktop_notification_settings_request_dict = update_chat_desktop_notification_settings_request_instance.to_dict()
# create an instance of UpdateChatDesktopNotificationSettingsRequest from a dict
update_chat_desktop_notification_settings_request_from_dict = UpdateChatDesktopNotificationSettingsRequest.from_dict(update_chat_desktop_notification_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


