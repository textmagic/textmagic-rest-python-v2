# UpdateBalanceNotificationSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low_balance_notification** | **bool** | Should user receive low balance notification. | [optional] 
**alert_balance** | **str** | If balance is below this value, user receive low balance notification. | [optional] 
**alert_phone** | **str** | Low balance notification phone number. | [optional] 
**alert_email1** | **str** | Low balance notification email 1. | [optional] 
**alert_email2** | **str** | Low balance notification email 2. | [optional] 
**alert_email3** | **str** | Low balance notification email 3. | [optional] 

## Example

```python
from TextMagic.models.update_balance_notification_settings_request import UpdateBalanceNotificationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBalanceNotificationSettingsRequest from a JSON string
update_balance_notification_settings_request_instance = UpdateBalanceNotificationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBalanceNotificationSettingsRequest.to_json())

# convert the object into a dict
update_balance_notification_settings_request_dict = update_balance_notification_settings_request_instance.to_dict()
# create an instance of UpdateBalanceNotificationSettingsRequest from a dict
update_balance_notification_settings_request_from_dict = UpdateBalanceNotificationSettingsRequest.from_dict(update_balance_notification_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


