# UpdateInboundMessagesNotificationSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_message_notification** | **bool** | Should user receive notification about new incoming messages. | [optional] 
**include_sms_history** | **bool** | Include SMS history into notification Email. | [optional] 
**send_in_html_format** | **bool** | Send Email notification in HTML format. | [optional] 
**alert_email1** | **str** | New message notification email 2. | [optional] 
**alert_email2** | **str** | New message notification email 2. | [optional] 
**alert_email3** | **str** | New message notification email 3. | [optional] 

## Example

```python
from TextMagic.models.update_inbound_messages_notification_settings_request import UpdateInboundMessagesNotificationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInboundMessagesNotificationSettingsRequest from a JSON string
update_inbound_messages_notification_settings_request_instance = UpdateInboundMessagesNotificationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInboundMessagesNotificationSettingsRequest.to_json())

# convert the object into a dict
update_inbound_messages_notification_settings_request_dict = update_inbound_messages_notification_settings_request_instance.to_dict()
# create an instance of UpdateInboundMessagesNotificationSettingsRequest from a dict
update_inbound_messages_notification_settings_request_from_dict = UpdateInboundMessagesNotificationSettingsRequest.from_dict(update_inbound_messages_notification_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


