# ContactCustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**user_custom_field** | [**UserCustomField**](UserCustomField.md) |  | [optional] 

## Example

```python
from TextMagic.models.contact_custom_field import ContactCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCustomField from a JSON string
contact_custom_field_instance = ContactCustomField.from_json(json)
# print the JSON string representation of the object
print(ContactCustomField.to_json())

# convert the object into a dict
contact_custom_field_dict = contact_custom_field_instance.to_dict()
# create an instance of ContactCustomField from a dict
contact_custom_field_from_dict = ContactCustomField.from_dict(contact_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


