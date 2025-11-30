# UpdateSenderSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Available phone number in international E.164 format or senderid. | [optional] 
**country** | **str** | Country for which the setting will be set. | [optional] 
**chat_id** | **int** | Set sender setting for specified chat only. | [optional] 

## Example

```python
from TextMagic.models.update_sender_setting_request import UpdateSenderSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSenderSettingRequest from a JSON string
update_sender_setting_request_instance = UpdateSenderSettingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSenderSettingRequest.to_json())

# convert the object into a dict
update_sender_setting_request_dict = update_sender_setting_request_instance.to_dict()
# create an instance of UpdateSenderSettingRequest from a dict
update_sender_setting_request_from_dict = UpdateSenderSettingRequest.from_dict(update_sender_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


