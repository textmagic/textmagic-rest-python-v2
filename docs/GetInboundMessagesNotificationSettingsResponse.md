# GetInboundMessagesNotificationSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_message_notification** | **bool** | Should user receive notification about new incoming messages. | 
**forwarded_call_notification** | **bool** | Should user receive notification about new forwarded calls. | 
**include_sms_history** | **bool** | Include SMS history into notification Email. | 
**send_in_html_format** | **bool** | Send Email notification in HTML format. | 
**alert_email1** | **str** | New message notification email 1. | 
**alert_email2** | **str** | New message notification email 2. | 
**alert_email3** | **str** | New message notification email 3. | 

## Example

```python
from TextMagic.models.get_inbound_messages_notification_settings_response import GetInboundMessagesNotificationSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInboundMessagesNotificationSettingsResponse from a JSON string
get_inbound_messages_notification_settings_response_instance = GetInboundMessagesNotificationSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetInboundMessagesNotificationSettingsResponse.to_json())

# convert the object into a dict
get_inbound_messages_notification_settings_response_dict = get_inbound_messages_notification_settings_response_instance.to_dict()
# create an instance of GetInboundMessagesNotificationSettingsResponse from a dict
get_inbound_messages_notification_settings_response_from_dict = GetInboundMessagesNotificationSettingsResponse.from_dict(get_inbound_messages_notification_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


