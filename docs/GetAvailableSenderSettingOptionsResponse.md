# GetAvailableSenderSettingOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated** | **List[str]** | Array of dedicated number strings. | 
**user** | **List[str]** | Array of verified account phone numbers (currently only one). | 
**shared** | **List[str]** | Array of shared number strings. | 
**sender_ids** | **List[str]** | Array of alphanumeric sender IDs. | 
**user_carrier_twilio** | **List[str]** | Array of alphanumeric sender IDs. | 
**user_carrier_vonage** | **List[str]** | Array of alphanumeric sender IDs. | 
**user_carrier_sinch** | **List[str]** | Array of alphanumeric sender IDs. | 
**u_carrier_bandwidth** | **List[str]** | Array of alphanumeric sender IDs. | [optional] 
**uc_twilio_sender_id** | **List[str]** | Array of alphanumeric sender IDs. | [optional] 

## Example

```python
from TextMagic.models.get_available_sender_setting_options_response import GetAvailableSenderSettingOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableSenderSettingOptionsResponse from a JSON string
get_available_sender_setting_options_response_instance = GetAvailableSenderSettingOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableSenderSettingOptionsResponse.to_json())

# convert the object into a dict
get_available_sender_setting_options_response_dict = get_available_sender_setting_options_response_instance.to_dict()
# create an instance of GetAvailableSenderSettingOptionsResponse from a dict
get_available_sender_setting_options_response_from_dict = GetAvailableSenderSettingOptionsResponse.from_dict(get_available_sender_setting_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


