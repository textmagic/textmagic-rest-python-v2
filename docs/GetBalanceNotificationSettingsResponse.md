# GetBalanceNotificationSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low_balance_notification** | **bool** | Should user receive low balance notification. | 
**alert_balance** | **float** | If balance is below this value, user receive low balance notification. | 
**alert_phone** | **str** | Low balance notification phone number. | 
**alert_email1** | **str** | Low balance notification email 1. | 
**alert_email2** | **str** | Low balance notification email 2. | 
**alert_email3** | **str** | Low balance notification email 3. | 

## Example

```python
from TextMagic.models.get_balance_notification_settings_response import GetBalanceNotificationSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalanceNotificationSettingsResponse from a JSON string
get_balance_notification_settings_response_instance = GetBalanceNotificationSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBalanceNotificationSettingsResponse.to_json())

# convert the object into a dict
get_balance_notification_settings_response_dict = get_balance_notification_settings_response_instance.to_dict()
# create an instance of GetBalanceNotificationSettingsResponse from a dict
get_balance_notification_settings_response_from_dict = GetBalanceNotificationSettingsResponse.from_dict(get_balance_notification_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


