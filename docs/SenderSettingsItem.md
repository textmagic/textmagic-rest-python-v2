# SenderSettingsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The 2-letter ISO country code of the recipient&#39;s phone number.  | 
**phone** | **str** | Phone enabled for sending to a specified country. | 

## Example

```python
from TextMagic.models.sender_settings_item import SenderSettingsItem

# TODO update the JSON string below
json = "{}"
# create an instance of SenderSettingsItem from a JSON string
sender_settings_item_instance = SenderSettingsItem.from_json(json)
# print the JSON string representation of the object
print(SenderSettingsItem.to_json())

# convert the object into a dict
sender_settings_item_dict = sender_settings_item_instance.to_dict()
# create an instance of SenderSettingsItem from a dict
sender_settings_item_from_dict = SenderSettingsItem.from_dict(sender_settings_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


