# UpdateCustomFieldValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | Contact ID. See [Contact](https://docs.textmagic.com/#tag/Contacts).  | [optional] 
**value** | **str** | Custom field value. Note that this value is not parsed in any way; it is stored and used in dynamic fields exactly as you send it. | [optional] 

## Example

```python
from TextMagic.models.update_custom_field_value_request import UpdateCustomFieldValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldValueRequest from a JSON string
update_custom_field_value_request_instance = UpdateCustomFieldValueRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldValueRequest.to_json())

# convert the object into a dict
update_custom_field_value_request_dict = update_custom_field_value_request_instance.to_dict()
# create an instance of UpdateCustomFieldValueRequest from a dict
update_custom_field_value_request_from_dict = UpdateCustomFieldValueRequest.from_dict(update_custom_field_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


