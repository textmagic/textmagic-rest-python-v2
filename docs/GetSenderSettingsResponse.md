# GetSenderSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**List[SenderSettingsItem]**](SenderSettingsItem.md) |  | 
**special** | [**List[SenderSettingsItem]**](SenderSettingsItem.md) |  | 
**other** | [**List[SenderSettingsItem]**](SenderSettingsItem.md) |  | 

## Example

```python
from TextMagic.models.get_sender_settings_response import GetSenderSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderSettingsResponse from a JSON string
get_sender_settings_response_instance = GetSenderSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSenderSettingsResponse.to_json())

# convert the object into a dict
get_sender_settings_response_dict = get_sender_settings_response_instance.to_dict()
# create an instance of GetSenderSettingsResponse from a dict
get_sender_settings_response_from_dict = GetSenderSettingsResponse.from_dict(get_sender_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


